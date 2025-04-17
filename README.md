# 🧠 RAG LangChain API (FastAPI + Huggingface)

Hệ thống Retrieval-Augmented Generation (RAG) dùng mô hình ngôn ngữ HuggingFace kết hợp LangChain và FastAPI.

---

## 🚀 Cài đặt

### 1. Clone repo và cài môi trường

```bash
git clone https://github.com/theanh9911/PDF-Question-Answering-with-LangChain-and-RAG
cd rag_langchain
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 2. Chạy server FastAPI
```bash
uvicorn src.app:app --host 0.0.0.0 --port 8080 --reload
```
#### Cấu trúc thư mục
```css
rag_langchain/
│
├── data_source/
│   └── generative_ai/
│       └── download.py
│
├── src/
│   ├── base/
│   │   └── llm_model.py
│   ├── rag/
│   │   ├── file_loader.py
│   │   ├── main.py
│   │   ├── offline_rag.py
│   │   ├── utils.py
│   │   └── vectorstore.py
│   └── app.py
│
├── requirements.txt
└── README.md
```
## 📡 API Endpoint
```bash
POST http://localhost:8080/generative_ai/playground/

{
  "question": "LangChain hoạt động như thế nào?"
}
```
## ⚙️ Mặc định đang dùng mô hình nhẹ flan-t5-small. Có thể thay đổi trong llm_model.py.


###### Demo
![image](https://github.com/user-attachments/assets/0bbbd251-18ad-4306-85e1-306d40364562) ![image](https://github.com/user-attachments/assets/52ee9855-e9be-41c5-b452-151e276b7916)


