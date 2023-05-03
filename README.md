Last Edit: 2023-05-03 11:28


This project is still under heavy development.

## About The Project
this project
- utilizes [Pinecone](https://www.pinecone.io/) vector database (VDB) and OpenAI (vector) embedding model to turn texts into vectors.
- The main program works with any `.md` file, so it works perfectly with Notion & Obsidian (though for. Notion you have to export it to `.md` manually first)
- is the author's practice of [Feynman technique](https://en.wikipedia.org/wiki/Learning_by_teaching).
- is probably a weaker duplicate of [llama_index](https://github.com/jerryjliu/llama_index#-dependencies), if you want a beautifully-creafted document query service, you should use llama_index instead of this toy.

## Walkthough of the Logic Behind this Program
1. Prepare the markdown (`.md`) files.
2. For each `.md` file, they will be vector embedded using OpenAI's embedding model.
3. The vectors are then uploaded to Pinecone vector database.
4. Queries are also converted to vectors using OpenAI's vector embedding model and uploaded to Pinecone.
5. To retrieve search results, we compare the query vector with vector database using Pinecone (by cosine similarity).
6. Top 3 results are returned and fed into GPT-3 with the question, and GPT-3 will generate an answer (in natural language).
7. App would be deployed on Streamlit.
8. And the Streamlit app would be embedded into Notion (so you can use these functions in notion)
## Getting Started

### Prerequisites
1. Prepare Pinecone API key and OpenAI API key
    - Pinecone API key can be obtained from [here](https://app.pinecone.io/).
    - OpenAI API key can be obtained from [here](https://platform.openai.com/account/api-keys).
2. export the Pinecone and OpenAI API key to system environment using
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
1. clone this repo to your local machine
    ```bash
    git clone https://github.com/madeyexz/notion-obsidian-csv-query.git
    ```
2. Install the dependencies
    ``` bash
    pip install pinecone langchain tqdm
    ```

### Usage
1. Prepare the markdown files and put them in a folder called `Notion_DB` (or any name you like, but you have to change the code accordingly). It should be in the same directory as `main.py`.
2. Run the program
    ``` bash
    python3 main.py PATH_TO_DOCS QUESTION
    ```
3. The query results and the reference GPT used to generate the answer will be saved in `answer.txt` and `contents.txt` respectively.


## Known Limitation
1. If you use Pinecone, then whenever you want to query a new document (i.e. creating a new database), you should create a new Pinecone index, or delete the old index. This is because Pinecone does not support updating the index (yet). 

    To do so
    ``` bash
    python3 delete_pinecone_index.py NAME_OF_INDEX
    ```
2. For each query, you have to upload and embed everything again. 
**This would be addressed soon. `query_only.md` is under heavy dev**
## Acknowledgements
Huge shout out to the open-source couumnity for providing straight-forward examples and comprehensive tutorials!
- [openai-cookbook: using vector database for embeddings search](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb)
- [Build a Personal Search Engine Web App using Open AI Text Embeddings - Avra](https://medium.com/@avra42/build-a-personal-search-engine-web-app-using-open-ai-text-embeddings-d6541f32892d)
- this project is heavily inspired by [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)
- [Langchain](https://python.langchain.com/en/latest), a Python library for manipulating LLMs elegently.
