from typing import Union, Optional
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


class VectorDB:
    def __init__(
        self,
        documents: Optional[list[Document]] = None,
        vector_db: Union[type(Chroma), type(FAISS)] = Chroma,
        embedding=HuggingFaceEmbeddings(),
    ) -> None:
        self.vector_db = vector_db
        self.embedding = embedding
        self.db = self._build_db(documents) if documents else None

    def _build_db(self, documents: list[Document]):
        db = self.vector_db.from_documents(documents=documents, embedding=self.embedding)
        return db

    def get_retriever(
        self,
        search_type: str = "similarity",
        search_kwargs: dict = {"k": 10}
    ):
        if self.db is None:
            raise ValueError("VectorDB is not initialized with any documents.")
        return self.db.as_retriever(search_type=search_type, search_kwargs=search_kwargs)
