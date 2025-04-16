import torch
from transformers import BitsAndBytesConfig, AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline

# Cấu hình 4‑bit NF4
nf4_config = BitsAndBytesConfig(
    load_in_4bit=True,                   # bật 4‑bit
    bnb_4bit_quant_type="nf4",           # kiểu NF4
    bnb_4bit_use_double_quant=True,      # bật double quantization (giảm lỗi)
    bnb_4bit_compute_dtype=torch.bfloat16  # dtype tính toán (float16 hoặc bfloat16)
)

def get_hf_llm(
    model_name: str = "google/flan-t5-small",     # thay bằng model bạn muốn
    max_new_tokens: int = 1024,
    **kwargs
):
    # Load model với cấu hình 4‑bit
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        low_cpu_mem_usage=True
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tạo pipeline text-generation
    model_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
        device_map="auto"
    )

    # Bọc vào LangChain
    llm = HuggingFacePipeline(
        pipeline=model_pipeline,
        model_kwargs=kwargs
    )
    return llm
