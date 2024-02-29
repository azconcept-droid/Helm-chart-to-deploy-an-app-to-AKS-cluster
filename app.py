from flask import Flask, jsonify
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import base64

load_dotenv()  # This line brings all environment variables from .env into os.environ

# Env variables
account_name = os.environ['ACCOUNT_NAME']
account_key = os.environ['ACCOUNT_KEY']
container_name = os.environ['CONTAINER_NAME']
blob_account_url = os.environ['BLOB_ACCOUNT_URL']


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_blob_contents():
    try:
        # Connect to Azure Blob Storage
        blob_service_client = BlobServiceClient(account_url=blob_account_url, credential=account_key)
        container_client = blob_service_client.get_container_client(container_name)

        # List all blobs in the container
        blobs = [blob.name for blob in container_client.list_blobs()]

        # Fetch contents of each blob
        blob_contents = {}
        for blob_name in blobs:
            blob_client = container_client.get_blob_client(blob_name)
            # Convert bytes to base64 string
            blob_data = base64.b64encode(blob_client.download_blob().readall()).decode('utf-8')
            blob_contents[blob_name] = blob_data

        return jsonify(blob_contents)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
