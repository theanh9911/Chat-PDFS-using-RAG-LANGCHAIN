import re
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


class Str_OutputParser(StrOutputParser):
    def __init__(self) -> None:
        super().__init__()

    def parse(self, text: str) -> str:
        return self.extract_answer(text)

    def extract_answer(self, text_response: str, pattern: str = r"Answer:\s*(.*)") -> str:
        match = re.search(pattern, text_response, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            return text_response


class Offline_RAG:
    def __init__(self, llm) -> None:
        self.llm = llm
        self.prompt = hub.pull("rlm/rag-prompt")
        self.str_parser = Str_OutputParser()

    def format_docs(self, docs) -> str:
        return "\n\n".join(doc.page_content for doc in docs)

    def get_chain(self, retriever):
        # Compose RAG pipeline using LangChain Runnables
        rag_chain = {
            "context": retriever | self.format_docs,
            "question": RunnablePassthrough()
        } | self.prompt | self.llm | self.str_parser

        return rag_chain
