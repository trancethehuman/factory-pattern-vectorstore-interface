from abc import ABC, abstractmethod


class VectorStoreBase(ABC):
    @abstractmethod
    def create_index(self, index_name):
        pass

    @abstractmethod
    def list_indexes(self):
        pass

    @abstractmethod
    def upsert_vector(self, index_name, vector_id, vector, metadata):
        pass

    @abstractmethod
    def query_index(self, index_name, query, metadata_filter):
        pass


class VectorStoreFactory:
    def __init__(self):
        self._creators = {}

    def register_type(self, key, creator):
        self._creators[key] = creator

    def get_vectorstore(self, key):
        creator = self._creators.get(key)
        if not creator:
            raise ValueError('Unsupported vectorstore type')
        return creator()
