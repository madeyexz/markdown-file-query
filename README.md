Latest Edit: 2023-04-19 14:39

## About The Project
this project
- utilizes [pinecone](https://www.pinecone.io/) database and OpenAI vector embedding model to embed and later query contents in Notion & Obsidian (`.csv` format files).
- is the author's practice of [Feynman technique](https://en.wikipedia.org/wiki/Learning_by_teaching).

## Rough Overview
1. Notion/Obsidian files are converted into `.csv` file
   1. TODO How to query the entire notion database?? 
2. For each `.csv` file, they will be vector embedded using OpenAI's vector embedding model.
3. The vector embedding is then uploaded to Pinecone database.
4. Queries are also vector embedded using OpenAI's vector embedding model.
5. Compare the vector embedding of the query with the vector embedding of the contents in Pinecone database using cosine similarity.
6. Return the top 3 results, and pip the first result into GPT-3 to generate a natural language response of the query
7. Deploy the app using Streamlit
8. Embed the Steamlit app into Notion

## Getting Started

### Prerequisites

### Installation


## Usage


## Acknowledgements
- [openai-cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb), huge shout out to this straight-forward and comprehensive cookbook.
- [Build a Personal Search Engine Web App using Open AI Text Embeddings - Avra](https://medium.com/@avra42/build-a-personal-search-engine-web-app-using-open-ai-text-embeddings-d6541f32892d)
- this project is heavily inspired by [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)
- The entire open-source community :)
