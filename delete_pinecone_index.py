import pinecone
import os
import sys

pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment="us-east1-gcp"
    )

index_name = sys.argv[1]

if index_name in pinecone.list_indexes():
    pinecone.delete_index(index_name)
    print(f"index: '{index_name}' successfully deleted")
else:
    print(f"index: '{index_name}' not found in pinecone")