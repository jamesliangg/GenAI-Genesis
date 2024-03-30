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
