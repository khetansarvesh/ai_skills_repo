`Situation :` Currently ROMA can only take text as input and find answers but we wanted it to take both text and image as input.

- [ UNIMODAL SEARCH ] text input ⇒ LLMs are used
- [ MULITMODAL SEARCH] image + text input ⇒ VLMs would be needed

`Task :`

- Now I can simply convert all the agents in ROMA into a VLM and pass image information to each agent. But here is the problem with it :
  - VLM will take higher time hence latency increases
  - Cost increases since more tokens will be used

Task: "Compare these 2 images"

API Call 1: Atomizer → sends 2 images (~4000 tokens each = 8K tokens)
API Call 2: Planner → sends 2 images again (8K tokens)
API Call 3: Executor #1 → sends 2 images again (8K tokens)
API Call 4: Executor #2 → sends 2 images again (8K tokens)
API Call 5: Aggregator → sends 2 images again (8K tokens)
API Call 6: Verifier → sends 2 images again (8K tokens)

Total: 48K+ tokens just for images, sent 6 times redundantly!

- Potential Optimizations
  - Lower Resolution for Some Agents: Atomizer could use a thumbnail; Executor gets full resolution
    - Though passing lower resolution image reduces cost and latency but will also lead to accuracy drop, question is does all the agents needs to see the images?
    - Does all the agents need a VLM or we can do a combination of LLM and VLM?
  - Text Summaries Instead: use a seperate llm to describe images and then pass this image information to agents in ROMA as text descriptions
    - Now this is a hacky way to represent image information but it misses the image text attention computation due to which both of them are not grounded and will also lead to accuracy drop !
    - This will lead to all ROMA agents to be an LLM, but instead can we combine some agents to be a LLM and others to be VLM?
  - Selective Image Passing: Not all agents need images
    - For instance a atomizer and a aggregator wont really require image information right !
    - But what about a planner? for some queries a planner agent might need it while for other query it might not
  - File Storage System : store the image in the file and access it only when required using a tool call. Let the llm reason when it needs it. Hence we will convert all ROMA agents to a VLM with tool calling capability ! When the image tool is called then VLM acts like a VLM and we use its image capabilities but when the image tool is not called then VLM acts like an LLM.

`Action :`

- But this requires all the ROMA agents to support tool calling, currently only the executor node supports tool calling
- Hence we have to change the ROMA agents definition?

`Result`

- if images are passed to llm then tokens would be 1000+ but now since we are storing it in file storage system (passing only the file storage path 20+) and passing it only on demand hence we are saving cost per LLM cost. Hence 95% token efficiency
- By implementing lazy image loading via tool calls, we reduce image token usage by 67-83% (from 48K to 8-16K tokens per query). This also reduces latency since fewer API calls process images.

Prepare for these:
Question: "Why not just use text descriptions of images?"
Your Answer Should Include: Loses visual grounding, cross-modal attention is important for accuracy
────────────────────────────────────────
Question: "How does DSPy handle images?"
Your Answer Should Include: dspy.Image class, format() method returns OpenAI-compatible content blocks, special markers for
serialization
────────────────────────────────────────
Question: "What if the LLM forgets to call the tool?"
Your Answer Should Include: Need strong prompting, could add validation layer
────────────────────────────────────────
Question: "Did you benchmark the accuracy difference?"
Your Answer Should Include: (Be honest - did you? If not, say it's future work)
────────────────────────────────────────
Question: "Why not use provider-side caching (like Gemini File API)?"
Your Answer Should Include: Provider-specific, tool approach is provider-agnostic
