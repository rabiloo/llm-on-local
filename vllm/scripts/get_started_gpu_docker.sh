docker run -itd --rm --runtime nvidia --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-p 8000:8000 \
-e MAX_BATCH_SIZE=16 -e BATCH_TIMEOUT_MS=100 \
vllm/vllm-openai:latest \
--model Qwen/Qwen2-1.5B-Instruct \
--tokenizer-mode auto \
--gpu-memory-utilization 0.8 \
--max-model-len 16384
