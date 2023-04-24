Last Edit: 2023-04-24 08:24
This project is still under heavy development.

## About The Project
this project
- utilizes [pinecone](https://www.pinecone.io/) database and OpenAI vector embedding model to embed and later query contents in Notion & Obsidian (`.csv` format files).
- is the author's practice of [Feynman technique](https://en.wikipedia.org/wiki/Learning_by_teaching).

## Rough Overview

1. Notion/Obsidian files are converted into `.md` file
2. For each `.md` file, they will be vector embedded using OpenAI's embedding model.
3. The vectors are then uploaded to Pinecone vector database.
4. Queries are also converted to vectors using OpenAI's vector embedding model and uploaded to Pinecone.
5. To retrieve search results, we compare the query vector with vector database using Pinecone (by cosine similarity).
6. Top 3 results are returned and fed into GPT-3 with the question, and GPT-3 will generate an answer (in natural language).
7. App would be deployed on Streamlit.
8. And the Streamlit app would be embedded into Notion (so you can use these functions in notion)
## Getting Started

### Prerequisites
1. Install the dependencies
    ``` bash
    pip install pinecone openai langchain tqdm
    ```
2. Prepare Pinecone API key and OpenAI API key
    - Pinecone API key can be obtained from [here](https://app.pinecone.io/).
    - OpenAI API key can be obtained from [here](https://platform.openai.com/account/api-keys).
3. export the Pinecone and OpenAI API key to system environment using
   ``` bash
   export PINECONE_API_KEY="your_pinecone_api_key"
   export OPENAI_API_KEY="your_openai_api_key"
   ```
   now in Python use
   ``` python
   import os
   os.environ["PINECONE_API_KEY"]
   os.environ["OPENAI_API_KEY"]
   ```
   to check if you have them exported to system environment, if `KeyError`, then restart the terminal upon completion (and your IDE if you are using one).
### Installation


## Usage


## Acknowledgements
- [openai-cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb), huge shout out to this straight-forward and comprehensive cookbook.
- [Build a Personal Search Engine Web App using Open AI Text Embeddings - Avra](https://medium.com/@avra42/build-a-personal-search-engine-web-app-using-open-ai-text-embeddings-d6541f32892d)
- this project is heavily inspired by [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)
- The entire open-source community :)
