# Overview

1. Notion/Obsidian files are converted into `.csv` file
   1. TODO How to query the entire notion database?? 
2. For each `.md` file, they will be vector embedded using OpenAI's vector embedding model.
3. The vector embedding is then uploaded to Pinecone database.
4. Queries are also converted to vectors using OpenAI's vector embedding model.
5. Compare the query vector with vector database using Pinecone (by cosine similarity).
6. Return the top 3 results, and prompt GPT-3 to answer the query with these returned materials.
7. Deploy the app on Streamlit
8. Embbed the Steamlit app into Notion.



### Regarding Dealing With the Raw Data
- Notion documents are exported without images, into `.zip` file. Which is later unzipped into a `.md` file.
- A linux command is used to get rid of quotation mark in the `.md` file.
   ``` bash
   sed 's/`//g' *.md
   ```

