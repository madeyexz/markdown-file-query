[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/madeyexz/markdown-file-query/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-blue.svg)](https://github.com/madeyexz/markdown-file-query/blob/main/README.zh.md)

## 概述
本项目
- 使用[Pinecone](https://www.pinecone.io/)向量数据库以及OpenAI的embedding model将文字转变为向量。
- 兼容任何`.md`类型文件，因此它完美兼容Notion和Obsidian（如果你用Notion的话得要手动输出成`.md`类型文件）
- 是作者使用[费曼学习法](https://en.wikipedia.org/wiki/Learning_by_teaching)的一个案例
- 可能是[llama_index](https://github.com/jerryjliu/llama_index#-dependencies)的一个弱化克隆。因此如果你想要一个撰写地更优美的文件问答程序，那么请参考llama_index。

### 实现原理
1. 对于每一个`.md`文件，它们会被`langchain.textsplitter`切分成许多小块。
2. 对于每一个小块，它们会被OpenAI的embedding model转换成向量(`langchain.embeddings.OpenAIEmbeddings`)
3. 接下来这些向量会被上传到`Pinecone`向量数据库。
4. 问题也会被转换成向量并上传到Pinecone。
5. 我们比较问题向量和数据库中的向量（使用余弦相似度）来检索结果。
6. 最相似的三个结果会被送入GPT-3，GPT-3会生成一个自然语言答案。

### 代办
- [ ] 加一个 `--help` 选项
- [ ] 部署到 Streamlit 上
## 开始

### 运行条件
1. 准备 Pinecone 和 OpenAI 的 API key
   - Pinecone API key 可以从[这里](https://app.pinecone.io/)获得。
   - OpenAI API key 可以从[这里](https://platform.openai.com/account/api-keys)获得。
2. 将 Pinecone 和 OpenAI 的 API key 导出到系统环境中
   ``` bash
   export PINECONE_API_KEY="your_pinecone_api_key"
   export OPENAI_API_KEY="your_openai_api_key"
   ```
   现在在 Python 中使用
   ``` python
   import os
   os.environ["PINECONE_API_KEY"]
   os.environ["OPENAI_API_KEY"]
   ```
   来检查你是否已经将它们导出到系统环境中，如果出现 `KeyError`，那么请重启终端（如果你在使用的话，还有你的IDE）。

### 安装
1. 将本项目克隆到你的本地
    ```bash
    git clone https://github.com/madeyexz/markdown-file-query.git
    ```
2. 安装依赖项
    ``` bash
    pip install pinecone langchain tqdm
    ```

### 使用
1. 准备好你的`.md`文件并将它们放在一个文件夹中（或者你可以自己取一个名字，但是你需要相应地修改代码）。注意这个文件夹应该和`main.py`在同一个目录下。
2. 如果这是你第一次查询某个文档，那么运行`main.py`程序
    ``` bash
    python3 main.py "文件夹的路径" "问题"
    ```
3. 查询结果和GPT生成答案的参考文本会分别保存在`answer.txt`和`contents.txt`中。
4. 如果你想要再次查询同一批文档，那么运行`query_only.py`来避免重新嵌入文档。
    ``` bash
    python3 query_only.py "问题"
    ```

### 使用实例
1. 我有一个文件夹叫做`markdown_database`，它包含了许多`.md`文件，我想要用问题"what's the strange situation"来查询这个数据库。
    ``` bash
    ❯ python3 main.py "markdown_database" "what's the strange situation"                                                        
    ```     
    ```text             
    initiating pinecone index...
    digesting docs...
    uploading datas to pinecone...
    92%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████          | 60/65 [00:29<00:02,  1.87it/s]
    let's wait for 60 seconds to avoid RateLimitError... \(since im not a paid user\))
    100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 [01:00<00:00,  1.00s/it]
    100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 65/65 [01:32<00:00,  1.42s/it]
    querying pinecone...
    querying gpt...
    writing results to answer.txt and contents.txt
    done! the answer to 'what's the strange situation' is: '
    The Strange Situation is a standardized procedure devised by Mary Ainsworth in the 1970s to observe attachment security in children within the context of caregiver relationships. It applies to infants between the age of nine and 18 months and involves a series of eight episodes lasting approximately 3 minutes each, whereby a mother, child and stranger are introduced, separated and reunited. The procedure is used to observe the quality of a young child’s attachment to his or her mother, and can also be applied to other attachment figures, such as God, through the use of Emotionally Focused Therapy (EFT) and religious beliefs, such as the saying “there are no atheists in foxholes”.'
    ```
2. 如果我想要再次查询同一批文档，那么我可以使用`query_only.py`来避免重新嵌入文档。
    ``` bash
    ❯ python3 query_only.py "Who is Mary Ainsworth?"
    ```
    ``` text
    connecting to pinecone index...
    getting docs
    querying pinecone...
    querying gpt...
    done! the answer to 'Who is Mary Ainsworth?' is: '
    Mary Ainsworth was a developmental psychologist who devised the Strange Situation in the 1970s to observe attachment security in children within the context of caregiver relationships. The Strange Situation involves a series of eight episodes lasting approximately 3 minutes each, whereby a mother, child and stranger are introduced, separated and reunited. Ainsworth is also known for her observation that if you want to see the quality of a young child’s attachment to his or her mother, watch what the child does, not when Mother leaves, but when she returns. She is also known for her research on anxious babies and their inability to use their mothers as a secure base.'
    ```
## 已知问题
1. 如果你使用了Pinecone，那么每当你想要查询一个新的文档（也就是创建一个新的数据库）时，你应该创建一个新的Pinecone索引（因为你不想要来自旧文档的答案），或者删除旧索引。这是因为Pinecone目前还不支持更新索引。

    要删除旧索引：
    ``` bash
    python3 delete_pinecone_index.py NAME_OF_INDEX
    ```
## 致谢
非常感谢开源社区提供的简单明了的例子和全面的教程！
- [openai-cookbook: using vector database for embeddings search](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb)
- [Build a Personal Search Engine Web App using Open AI Text Embeddings - Avra](https://medium.com/@avra42/build-a-personal-search-engine-web-app-using-open-ai-text-embeddings-d6541f32892d)
- this project is heavily inspired by [hwchase17/notion-qa](https://github.com/hwchase17/notion-qa)
- [Langchain](https://python.langchain.com/en/latest), a Python library for manipulating LLMs elegently.
