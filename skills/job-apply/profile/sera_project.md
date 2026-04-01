# Summary

Building reliable AI agents for crypto research means coordinating dozens of tools under tight latency budgets. We started with vanilla ReAct — and quickly hit its limits. With 40+ tools in the action space, ReAct struggled with tool selection, wasted iterations on failures, and ran too slowly for production traffic. Over a series of experiments, we systematically solved each bottleneck: first by shrinking the action space with RAG-based tool filtering, then by parallelizing tool calls, and finally by combining both ideas into the architecture that paved the path to **SERA**.

This blog walks through the engineering journey — what broke, what we tried, and what the data told us — culminating in the design principles behind SERA, our Semantic Embedding & Reasoning Agent architecture described in our [previous blog](https://blog.sentient.xyz/posts/semantic-embeddings-reasoning-agent-crypto).

Key results:

- **RAG-based tool filtering** reduced tool failure rates by **29%** and improved tool efficiency by **20%**
- **Parallel tool calling** cut query latency by **40%** (31s → 18.5s)
- **Combining both** yielded **25% fewer tools per query** and **15% higher tool efficiency**, while **95% of queries completed in ≤2 iterations**
- These findings directly informed **SERA's** embedding-based routing, parallel execution, and optional second-pass architecture

---

## The Problem: ReAct Doesn't Scale With Large Tool Arsenals

ReAct is the default architecture for tool-using agents: think, pick a tool, observe the result, repeat. It works well when the agent has a handful of tools and the task is straightforward. But we were building a crypto research agent with **40+ tools** — market data APIs, TVL trackers, on-chain flow providers, derivatives feeds, social sentiment endpoints, and more.

At this scale, ReAct broke down in predictable ways. The LLM (GPT-OSS-120B) couldn't reliably select the right tool from such a large action space. It frequently picked wrong tools or passed incorrect parameters, causing tool failures that triggered additional iterations. Each failed iteration ate into our latency budget without producing useful information.

We needed to systematically address three compounding problems: **tool selection accuracy**, **execution latency**, and **the interaction between the two**.

---

## Experiment 1: Shrinking the Action Space with RAG

### The Idea

Instead of handing the LLM all 40+ tools and hoping it picks correctly, we added a **retrieval step** before tool selection. We embedded all tool descriptions and ran similarity search against the user query, filtering down to the **top 15 most relevant tools** before the LLM ever saw them.

### Setup

- **Baseline:** Vanilla ReAct with all 40+ tools exposed to GPT-OSS-120B
- **Variant:** RAG-filtered ReAct — same model, same loop, but only the top-15 retrieved tools are provided

### **Measuring Tool Efficiency**

Before diving into the results, we needed a metric that captures both the volume and reliability of tool usage in a single number. Standard metrics like "number of tool calls" or "failure rate" each tell only half the story — an agent that makes few calls but fails on all of them isn't efficient, and neither is one that succeeds on every call but makes dozens of unnecessary ones.

We introduced a **tool efficiency metric** that penalizes both excessive tool usage and tool failures:

```
tool_efficiency = (1 - total_tool_calls / 10) × (1 - tool_failure_rate)²
```

where `tool_failure_rate = total_failed_tools / total_tools_called` within the ReAct loop. The quadratic penalty on failure rate reflects our observation that tool failures are disproportionately costly — each failure not only wastes a step but often sends the agent down an unproductive reasoning path for subsequent iterations.

### Results

| Metric            | Vanilla ReAct | RAG ReAct | Improvement    |
| ----------------- | ------------- | --------- | -------------- |
| Tool failure rate | 13.17%        | 9.25%     | **29% lower**  |
| Avg tools / query | 5.58          | 4.63      | **17% fewer**  |
| Tool efficiency   | 0.394         | 0.473     | **20% higher** |

The aggregate gains were clear: fewer tools meant cleaner selection, fewer failures, and less wasted computation. But the averages mask an important pattern that only becomes visible when we break down results by iteration count.

### **The Three Zones: When RAG Helps (and When It Doesn't)**

The chart below plots the **tool efficiency difference** (RAG ReAct minus Vanilla ReAct) for each query, sorted by the number of ReAct iterations (purple line, right axis). Orange regions indicate queries where RAG ReAct outperformed; blue regions indicate where vanilla ReAct was better.

The data splits cleanly into three zones:

**Zone 1 — Low iterations (≤4 loops):** Vanilla ReAct performs equally or better. These are simple queries where the agent finds the right tool quickly regardless of action space size. RAG filtering adds a retrieval step without meaningful benefit — the LLM was already navigating the tool space fine.

**Zone 2 — Medium iterations (5–8 loops):** Mixed results. Neither architecture consistently dominates. These queries are complex enough that tool selection matters, but not so complex that vanilla ReAct completely fails. The advantage shifts back and forth depending on the specific query.

**Zone 3 — High iterations (>8 loops):** RAG ReAct clearly and consistently wins. These are the queries where vanilla ReAct spirals — repeatedly choosing wrong tools or passing bad parameters, burning through its entire iteration budget. By narrowing the action space, RAG filtering prevents the agent from getting lost in irrelevant tools and helps it converge much faster.

This three-zone pattern gave us a crucial insight: **the value of action space reduction scales with query complexity.** For simple queries, the LLM handles large tool sets fine. For complex queries, a smaller, curated tool set is the difference between a 3-iteration success and a 10-iteration failure.

We also observed something interesting in Zone 3: even when both architectures produced the _exact same reasoning_ (identical `THOUGHT` steps at a given iteration), RAG ReAct consistently selected the correct tool while vanilla ReAct did not. This suggests the issue isn't reasoning quality — it's the **cognitive load of a large action space** on tool selection.

---

## Experiment 2: Parallel Tool Calling

### The Idea

ReAct executes tool calls sequentially by design — the output of tool _n_ feeds the reasoning for tool _n+1_. This makes sense for multi-hop queries where each step depends on the last. But when we analyzed our production crypto traffic, we found that **most queries are not multi-hop**. A user asking "What's happening with SOL?" needs market data, sentiment, and on-chain flows fetched independently, not sequentially.

We built a **parallel ReAct agent** that identifies independent tool calls within a single reasoning step and executes them concurrently.

### Results

| Metric            | Sequential ReAct | Parallel ReAct | Improvement    |
| ----------------- | ---------------- | -------------- | -------------- |
| Avg query time    | 36.48s           | 21.33s         | **42% faster** |
| Median query time | 31.08s           | 18.59s         | **40% faster** |

A straightforward win: for non-multi-hop queries, parallel execution nearly halves latency.

---

## Experiment 3: Combining RAG Filtering + Parallel Execution

### The Idea

The natural next step: take our parallel ReAct agent and add RAG-based tool filtering on top. Does shrinking the action space still help when the agent is already executing in parallel?

### Results

| Metric                | Parallel ReAct | Parallel RAG ReAct | Improvement    |
| --------------------- | -------------- | ------------------ | -------------- |
| Avg tools / iteration | 3.83           | 2.80               | **27% fewer**  |
| Avg tools / query     | 4.77           | 3.42               | **28% fewer**  |
| Tool efficiency       | 0.413          | 0.474              | **15% higher** |

The iteration counts barely changed — both architectures already converge in 1–2 loops for most queries. But **tool efficiency improved meaningfully**: the RAG-filtered variant calls fewer tools per iteration and achieves higher efficiency, meaning it's doing less redundant work to arrive at the same quality answer.

We validated answer quality by measuring embedding similarity between the outputs of both systems: **0.85** — confirming that the RAG-filtered variant produces equivalent answers with less compute.

---

## The Path to SERA

These three experiments revealed a clear pattern in our production traffic:

1. **95% of queries complete in ≤2 iterations** — long ReAct loops are wasteful for our use case
2. **RAG-based tool selection consistently outperforms brute-force selection** in large action spaces
3. **Parallel execution dramatically cuts latency** for non-multi-hop queries
4. **Combining both** yields the best efficiency without sacrificing answer quality

This data directly motivated **SERA** (Semantic Embedding & Reasoning Agent), which we described in our [previous blog](https://blog.sentient.xyz/posts/semantic-embeddings-reasoning-agent-crypto). SERA crystallizes these findings into a production architecture:

- **Embedding-based tool routing** replaces the LLM-as-tool-selector pattern entirely, using vector similarity to match queries to tools — a more robust version of the RAG filtering tested here
- **Parallel execution by default**, since our data proved that sequential tool calling is unnecessary for the vast majority of crypto research queries
- **An optional second iteration with gap analysis**, preserving the ability to do a follow-up pass for the ~5% of queries that need it
- **Dynamic prompt selection** via a second embedding index, routing each query to the most relevant reasoning template

SERA is what you get when you take the empirical lessons from these experiments and design an architecture around them from the ground up, rather than bolting patches onto ReAct.

---

---

## When to Use What: A Practical Decision Framework

Our experiments point to a simple routing heuristic:

- **Use SERA** for the common case — single-pass queries that need fast, high-quality answers from multiple data sources. This covers ~95% of production crypto research traffic.

- **Use ReAct** when the query is genuinely multi-hop — where the output of one tool call must inform the next (e.g., "Find the top DeFi protocol by TVL on Arbitrum, then analyze its token distribution"). If the tool arsenal is large (20+ tools), layer in RAG-based tool filtering to improve selection accuracy.

The key insight is that **architecture should match query complexity**. Over-engineering simple queries with multi-step loops wastes latency and compute. Under-engineering complex queries with single-pass systems sacrifices answer quality. The right system routes each query to the lightest architecture that can handle it well.

---

- S : ReAct took a lot of time but gave good answers.
- T : for a user latency should be low, so we prioritised latency over good answers
- A : dynamic prompts (11 categories)

So in React 1 tool is called in each iteration (implies 5 tools in 5 iterations). This architecture makes sense when tool calls are dependent on each other. But when we saw what queries user were asking we saw parallel tool calls could be possible.

Hence we tried mini - ReAct. (issue was accuracy of tool calls were not so great and 80% queries answered in 1 iteration and 15% answered in 2nd)

Hence we restircted to 1 loop + RAG based tool calling. (+optional 2nd loop after gap analysis)

Now above used a reasoning LLM to answer but it was time consuming and costly due to reasoning tokens. The reasoning model did work well for 90% cases (had +10sec latency though) but 10% it gave counter arguments and then went on a loop => thus not giving right answers and taking more time too. Hence we decided to go with an instruct model. Problem with instruct model is that if a query needs 4 tool calls, it sometimes misses them. So based on user query complexity, we put the constraint to use 6 tool calls for 90 percentile of the queries, so it almost always does 6 tool calls for all the queries. (in entire pipeline we use OSS 120b except for the part where we want to do parallel tool calls we use a QWEN MODEL cause OSS 120b can only give 1 tool output)

added a caching layer (note I was not the part of the team that designed the cache layer)

- R : we create a SOTA crypto agent with lowest latency with similarity ratio with react based answer close to 0.9

Improvements :

**long context issue in SERA** (eg analyse correlation of btc and eth in last 1 year) data will consist of long numerics and hence we started experiementing with CodeAct (tool calling with via Code)

**optional web search** : SERA calls data apis and web search parallely. Improve latency by instead doing a sequential web search only for that information which was missing by data api layers.
