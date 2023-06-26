from vectorstore.blueprints import VectorStoreFactory
from vectorstore.pinecone_wrapper import PineconeVectorStore
from vectorstore.supabase_pgvector_wrapper import SupabaseVectorStore


# Create a factory and register the vectorstore type.
vectorstore_factory = VectorStoreFactory()
vectorstore_factory.register_type("pinecone", PineconeVectorStore)
vectorstore_factory.register_type("supabase", SupabaseVectorStore)

# Get a vectorstore instance from the factory.
vectorstore = vectorstore_factory.get_vectorstore("supabase")

# Assuming we have the following parameters
index_name = "example_index"
vector_id = "vector1"
vector = [0.1, 0.2, 0.3]
metadata = {"description": "example vector"}

# Upsert a vector
vectorstore.upsert_vector(index_name, vector_id, vector, metadata)

# List indexes
vectorstore.list_indexes()

# Define a query
query = {"type": "nearest", "vector": vector}

# Define a metadata_filter
metadata_filter = {"description": "example vector"}

# Run an index query.
vectorstore.query_index(index_name, query, metadata_filter)
