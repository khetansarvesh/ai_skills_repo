# Project Descriptions

> These descriptions are used for open-ended application questions like "Tell us about a project",
> "Why are you interested in this role?", "Describe a technical challenge you solved", etc.
> The skill will select and adapt the most relevant project/answer based on the question context.
> For full details, read the individual project files in this directory.

## Projects

### 1. ROMA — Recursive Deep Search Agent (Sentient)

- **File**: `roma_project.md`
- **Tech Stack**: DSPy, LLMs, parallel tool calling, dependency graphs
- **Duration**: Nov 2025 - Present
- **Summary**: Built ROMA, a recursive deep search agent for hierarchical problem solving. Surpassed SOTA by 10% on SEAL-0 benchmark.
- **Key Achievements**:
  - Replaced sequential ReAct executor with parallel tool calling, cutting latency significantly
  - Implemented dependency graph + cycle detection for intra-depth subagent communication
  - Optimized planner agent via prompt engineering and ReAct evaluator to eliminate repetitive task decomposition
- **Challenge & Solution**: Planner generated non-optimal plans with repetitive tasks. Built dependency graphs and added tool-aware prompting so the planner avoids redundant tool calls with same arguments.

### 2. SERA — Semantic Embedding & Reasoning Agent (Sentient)

- **File**: `sera_project.md`
- **Tech Stack**: RAG, embedding-based routing, parallel tool calling, GPT-OSS-120B, Qwen
- **Duration**: Nov 2025 - Present
- **Summary**: Designed SERA framework for a crypto research agent with 40+ tools. Achieved 90% behavioral similarity to ReAct with 50% inference latency drop and 30% fewer tool failures.
- **Key Achievements**:
  - RAG-based tool filtering reduced tool failure rates by 30% and improved tool efficiency by 20%
  - Parallel tool calling cut query latency by 40% (31s to 18.5s)
  - Combined RAG + parallel execution yielded 25% fewer tools per query and 15% higher efficiency
  - 95% of queries completed in 1-2 iterations vs 8+ with vanilla ReAct
- **Challenge & Solution**: Vanilla ReAct couldn't scale with 40+ tools — high failure rates, slow convergence. Systematically proved through 3 experiments that embedding-based tool routing + parallel execution solves this, then built SERA as production architecture.

### 3. m-ROMA — Multimodal ROMA (Sentient)

- **File**: `multimodal_roma_project.md`
- **Tech Stack**: Reference-based image handling, File Storage Toolkit
- **Duration**: Nov 2025 - Present
- **Summary**: Extended ROMA to handle multimodal inputs via reference-based image handling, achieving 95% token efficiency.
- **Key Achievements**:
  - Implemented reference system where images stored externally and referenced by ID
  - Only relevant metadata passed to LLM, dramatically reducing API costs
  - 95% token efficiency while maintaining output quality

### 4. Multi-Agent Deep Research System (Strategy)

- **File**: `strategy_deep_research.md`
- **Tech Stack**: LangGraph, ReAct, Azure Blob, RAG, LLM-as-a-Judge
- **Duration**: Jun 2025 - Aug 2025
- **Summary**: Optimized a multi-agent ReAct-style Deep Research system at Strategy (MicroStrategy), improving LLM response quality by 40%.
- **Key Achievements**:
  - Integrated planner agent with external tools for coordinated search via LangGraph
  - Built Azure Blob connector tool using RAG architecture for one-click ingestion of 1,000+ files across 10+ formats
  - Built long-context LLM evaluator using LLM-as-a-Judge and checklist scoring, achieving 94% agreement with human labels
- **Challenge & Solution**: Context bloat from mixing web search and internal tool results in a single ReAct agent. Moved to multi-agent architecture so each agent has its own separate context window.

### 5. RAG-based Text2SQL Graph AI Agent (Piramal Enterprises)

- **File**: `txt2sql_project.md`
- **Tech Stack**: LangChain, Knowledge Graphs, Neo4j, GNNs, Snowflake, Pinecone, LLMs (GPT-4, Claude-2, LLaMA)
- **Duration**: Jun 2022 - Aug 2024
- **Summary**: Designed a patented RAG-based Text2SQL agent that converts natural language to SQL using knowledge graphs and GNNs. Secured $1M+ in management funding.
- **Key Achievements**:
  - Built chain prompting pipeline: domain identification → table selection → key element extraction → code generation → answer synthesis
  - Used Graph Neural Networks on Neo4j knowledge graph for join condition resolution
  - Dynamic few-shot examples for improved SQL generation accuracy
  - Supported both Pandas generation and direct SQL execution on Snowflake
- **Challenge & Solution**: Join conditions between tables were the hardest part of SQL generation. Built a knowledge graph in Neo4j representing table relationships, then used GNN embeddings + Cypher queries to automatically determine correct joins.

## Reusable Answer Snippets

### Why are you interested in [company type]?

> Adapt per company. Write a base template here.

### What is your greatest strength?

> I combine deep AI/ML research skills with practical engineering to ship production systems. I've published papers and also built patented products that secured $1M+ funding. I bridge the gap between cutting-edge research and real-world deployment.

### Describe a time you worked on a team

> At Piramal, I led a team of 5 engineers to build a patented RAG-based Text2SQL agent. I designed the architecture, distributed workstreams (graph DB, prompt pipeline, evaluation), ran weekly syncs, and resolved technical disagreements by running comparative experiments. We delivered on time and secured $1M+ in continued funding.

### Why are you a good fit for this role?

> I bring 3+ years of hands-on experience building AI systems end-to-end — from research (ROMA beating SOTA by 10%, SERA reducing latency 50%) to production (multi-agent systems at Strategy, data pipelines at Piramal). I have a MS in ML from UMD (3.90 GPA) and a track record of shipping AI products that deliver measurable business impact.

### Anything else you'd like us to know?

> I'm deeply passionate about agentic AI systems. Beyond my work experience, I actively maintain an open-source AI skills repo, contribute to research on recursive search agents, and am always exploring the frontier of what AI agents can do autonomously.
