from fastapi import FastAPI
from flask_cors import CORS
from upload import initialize_database

app = FastAPI()
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow any origin


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
    response_json = list()
    for result in results:
        result_dict = dict()
        for meta_item in result[0].metadata:
            result_dict[meta_item] = result[0].metadata[meta_item]
            result_dict['similarity'] = result[1]
        response_json.append(result_dict)
    return {"query": f"{query}", "response": response_json}
