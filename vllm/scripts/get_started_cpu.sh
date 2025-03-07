git clone https://github.com/vllm-project/vllm.git vllm_source
cd vllm_source

# Build image for serving LLM on CPU
docker build -t vllm-cpu -f Dockerfile.cpu .

# Run docker container
docker run -itd --rm \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-p 8000:8000 \
-e MAX_BATCH_SIZE=16 \
vllm-cpu:latest \
--model Qwen/Qwen2-1.5B-Instruct \
--trust-remote-code \
--device cpu \
--dtype bfloat16 \
--tokenizer-mode auto
