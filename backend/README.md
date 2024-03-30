
## GCP
Steps to prepare a service account for Vertex AI. 
1. Go to the [Service Accounts ](https://console.cloud.google.com/iam-admin/serviceaccounts) page.
2. Select the project you want to use.
3. Create a service account. 
   - You only need to give the account a name under `1. Service account details` > `Service account name`
4. Create a new key. 
   - Click on the service account you just created. 
   - Click on `Add Key` > `Create new key`
   - Select `JSON` and click `Create`
5. Go to the [IAM](https://console.cloud.google.com/iam-admin/iam) page. 
6. Grant Access to the service account.
   - Add the following roles:
       - `Vertex AI User`
7. Upload the JSON key to `/backend` and rename it to `service_account.json`
## Running the app
Create a `.env` file in the root directory with similar to below
```markdown
redis_url={redis_url}
GOOGLE_APPLICATION_CREDENTIALS=service_account.json
```
To run app, `cd` into `/backend` and run `uvicorn main:app --reload`
## Endpoints
Documentation can be found at http://127.0.0.1:8000/docs.

There is only one GET endpoint http://127.0.0.1:8000/query/{query} where `{query}` is the search query.

It should respond with a JSON object with the following structure:
```json
{
    "query": "Software engineer",
    "response": [
        {
            "id": "doc:jobs:b9d44ed4b5d546d4a506537a8d497d0f",
            "similarity": 0.6681,
            "job_title": "Data Engineer",
            "location": "New York",
            "salary": "100000",
            "job_type": "Full Time",
            "description": "Data Engineer needed to build data pipelines and warehouses. Must have experience with Hadoop and Spark."
        }
    ]
}
```