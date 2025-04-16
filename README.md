# 🧠 RAG LangChain PDF QA API

Dự án này xây dựng một hệ thống **RAG (Retrieval-Augmented Generation)** để trả lời câu hỏi dựa trên tài liệu PDF bằng cách sử dụng:
- `LangChain`
- `HuggingFace Transformers`
- `FastAPI` (kết hợp LangServe để tạo playground tương tác)

---

## 📦 Cấu trúc thư mục

rag_langchain_prj/ │ ├── data_source/ │ └── generative_ai/ # Chứa các file PDF nguồn │ ├── src/ │ ├── app.py # FastAPI app chính │ ├── base/ │ │ └── llm_model.py # Hàm khởi tạo HuggingFace LLM │ └── rag/ │ ├── main.py # Build RAG chain │ └── file_loader.py # Load & split PDF │ ├── requirements.txt └── README.md


### 1. Cài đặt thư viện

```bash
pip install -r requirements.txt.
```
### 2. Chạy server
uvicorn src.app:app --host 0.0.0.0 --port 5000 --reload
