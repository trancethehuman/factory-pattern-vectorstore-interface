from blueprints import VectorStoreBase
from dotenv import load_dotenv
import os
import pinecone

load_dotenv()


class PineconeVectorStore(VectorStoreBase):
    def __init__(self):
        pinecone.init(
            api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_ENVIRONMENT"])
        self.client = pinecone
        print("Initialized Pinecone client")

    def list_indexes(self):
        return self.client.list_indexes()

    def create_index(self, index_name):
        # Implementation for Pinecone goes here...
        print("Creating index")

    def upsert_vector(self, index_name: str, vector_id, vector, metadata):

        # Implementation for Pinecone goes here...
        print("Upserting vector")

    def query_index(self, index_name, query, metadata_filter):
        # Implementation for Pinecone goes here...
        print("Querying index")
