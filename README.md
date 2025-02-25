# Crew AI with Azure

Your .env should look like this for Azure usage:

```
MODEL=gpt-4o
AZURE_API_BASE=https://YOURENDPOINT.openai.azure.com/
AZURE_API_VERSION=2024-08-01-preview
AZURE_AD_TOKEN=
```

Generate a token with code like:

```
from azure.identity import AzureDeveloperCliCredential
credential = AzureDeveloperCliCredential(tenant_id="e47e6fc9-3a2c-454a-8b8f-90cc6972fb77")
credential.get_token("https://cognitiveservices.azure.com/.default").token
```

Then run the code:

```
cd my_project
crewai install
crewai run
```
