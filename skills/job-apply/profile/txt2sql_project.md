Embedding Model : BERT / GPT

LLM : GPT3.5 / Claude-2 / LLama / GPT4 / Falcon / Open Pretrained Transformer (OPT) /

Convert tabular to Text

=> Stored embeddings in Vector DB => Pinecode => SIMILARITY SEARCH (RAG)

=> LLama Index

Code Generation :

— Few shots => Dynamic Few Shots

— Chain Prompting

=> LLM0 to identify which domain

=> LLM1 to identify tables

=> LLM2 identify key elements in question is RM / Branch / Zone / ….

=> LLM3 which did code generation to get context => input was table schema

=> LLM4 which used the context to answer query

a. Pandas generation =>

- worked well but we had to bring entire data to runtime (tried pandas implementation + langchain implementation + our own version)

b. SQL Generation => we could directly run this sql on the snowflake via api call and hence no need to bring data to runtime !!

Issue with join conditions

- Graph : generate cypher to get joins between tables

Langchain for experiment => given query and graph on neo4j it gave cypher query => at backend used the schema of the graph to generate query

Own implementation

a. Based on question use LLM to get the relevant nodes and relations and SCHEMA

b. Graph neural network to create embeddings

add dynamic few shots
