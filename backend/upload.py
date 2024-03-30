# https://python.langchain.com/docs/integrations/vectorstores/redis
# https://cloud.google.com/blog/products/databases/memorystore-for-redis-vector-search-and-langchain-integration
import os
import csv
import dotenv
import pickle
from langchain_community.vectorstores.redis import Redis
from langchain_google_vertexai import VertexAIEmbeddings

dotenv.load_dotenv()

REDIS_URL = os.getenv("redis_url")


def initialize_database() -> Redis:
    embedding = VertexAIEmbeddings(model_name="textembedding-gecko@001")
    index_name = "jobs"
    if os.path.isfile("vectorstore.pkl"):
        with open("vectorstore.pkl", "rb") as f:
            schema, key_prefix, index_name = pickle.load(f)
        vectorstore = Redis.from_existing_index(embedding=embedding, index_name=index_name, schema=schema,
                                                key_prefix=key_prefix, redis_url=REDIS_URL)
        print("Loaded existing vectorstore from file.")
    else:
        data = open_csv("test.csv")
        metadata = list()
        texts = list()
        for jobs in data:
            metadata.append({"job_title": jobs[0], "location": jobs[1], "salary": jobs[2], "job_type": jobs[3],
                             "description": jobs[4]})
            texts.append(jobs[4])
        vectorstore = Redis.from_texts(texts, embedding, metadatas=metadata, redis_url=REDIS_URL, index_name=index_name)
        with open("vectorstore.pkl", "wb") as f:
            pickle.dump([vectorstore.schema, vectorstore.key_prefix, vectorstore.index_name], f)
        print("Created new vectorstore from test file.")
    return vectorstore


def open_csv(file_name: str) -> list:
    with open(file_name, mode='r') as file:
        data = list(csv.reader(file))
        return data


def query_database(vectorstore: Redis, query: str, num_results: int = 5) -> list:
    results = vectorstore.similarity_search_with_relevance_scores(query, k=num_results)
    return results


# vectorstore = initialize_database()
# results = query_database(vectorstore, "developer software engineer", 3)
# print(results)
# for result in results:
#     print(f"Content: {result[0].page_content} --- Similiarity: {result[1]} --- Metadata: {result[0].metadata}")
