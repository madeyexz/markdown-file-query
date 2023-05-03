Last Edit: 2023-05-03 14:22

## About The Project
this project
- utilizes [Pinecone](https://www.pinecone.io/) vector database (VDB) and OpenAI (vector) embedding model to turn texts into vectors.
- The main program works with any `.md` file, so it works perfectly with Notion & Obsidian (though for Notion you have to export it to `.md` manually first)
- is the author's practice of [Feynman technique](https://en.wikipedia.org/wiki/Learning_by_teaching).
- is probably a weaker duplicate of [llama_index](https://github.com/jerryjliu/llama_index#-dependencies), if you want a beautifully-creafted document query service, you should use llama_index instead of this toy.

## Walkthough of this Program
1. For each `.md` file, they will be cut into lots of small chunks using `langchain.textsplitter`
2. For each chunk, it is vector embedded by OpenAI's embedding model (`langchain.embeddings.OpenAIEmbeddings`)
3. The vectors are then uploaded to `Pinecone` vector database.
4. Queries are also converted to vectors using OpenAI's vector embedding model and uploaded to Pinecone.
5. To retrieve search results, we compare the query vector with vector database using Pinecone (by cosine similarity).
6. Top 3 results are returned and fed into GPT-3 with the question, and GPT-3 will generate an answer (in natural language).

## TODO
- [ ] add a `--help` option
- [ ] deploy to Streamlit
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
1. Prepare the markdown file(s) and put them in a `FOLDER` (or any name you like, but you have to change the code accordingly). Notice this should be in the same directory as `main.py`.
2. If this is your first time querying a certain document, run the `main.py` program
    ``` bash
    python3 main.py "PATH_OF_FOLDER" "QUESTION"
    ```
3. The query results and the reference GPT used to generate the answer will be saved in `answer.txt` and `contents.txt` respectively.
4. If you want to query the same batch of documents again, then run the `query_only.py` to avoid re-embedding the documents.
    ``` bash
    python3 query_only.py "QUESTION"
    ```


## Known Limitation
1. If you use Pinecone, then whenever you want to query a new document (i.e. creating a new database), you should probably create a new Pinecone index (for you don't want answers from the old document), or delete the old index. This is because Pinecone does not support updating the index (yet). 

    To delete the old index:
    ``` bash
    python3 delete_pinecone_index.py NAME_OF_INDEX
    ```
## Acknowledgements
Huge shout out to the open-source couumnity for providing straight-forward examples and comprehensive tutorials!
- [openai-cookbook: using vector database for embeddings search](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb)
- [Build a Personal Search Engine Web App using Open AI Text Embeddings - Avra](https://medium.com/@avra42/build-a-personal-search-engine-web-app-using-open-ai-text-embeddings-d6541f32892d)
- this project is heavily inspired by [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)
- [Langchain](https://python.langchain.com/en/latest), a Python library for manipulating LLMs elegently.
