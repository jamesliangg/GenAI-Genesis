from fastapi import FastAPI
from upload import initialize_database

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/query/{query}")
async def query(query: str):
    vectordatabase = initialize_database()
    results = vectordatabase.similarity_search_with_relevance_scores(query, 5)
    response_json = dict()
    i = 0
    for result in results:
        response_json[i] = dict()
        for meta_item in result[0].metadata:
            response_json[i][meta_item] = result[0].metadata[meta_item]
            response_json[i]['similarity'] = result[1]
        i += 1
    return {"query": f"{query}", "response": response_json}
