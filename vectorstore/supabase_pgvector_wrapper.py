import os
from dotenv import load_dotenv
from vectorstore.blueprints import VectorStoreBase
from supabase.client import create_client
from typing import Optional


load_dotenv()


class SupabaseVectorStore(VectorStoreBase):
    def __init__(self):
        url: Optional[str] = os.getenv("SUPABASE_URL")
        key: Optional[str] = os.getenv("SUPABASE_KEY")

        if not url or not key:
            raise ValueError(
                "Missing Supabase URL or Key in environment variables.")

        self.client = create_client(url, key)

    def list_indexes(self):
        # Implementation for Supabase goes here...
        print("Listing all indexes")

    def create_index(self, index_name):
        # Implementation for Supabase goes here...
        print("Creating index")

    def upsert_vector(self, index_name: str, vector_id, vector, metadata):
        # Implementation for Supabase goes here...
        print("Upserting vector")

    def query_index(self, index_name, query, metadata_filter):
        # Implementation for Supabase goes here...
        print("Querying index")
