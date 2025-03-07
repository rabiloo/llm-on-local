# Make sure that you have installed python 3.8+ in your environment
python -m venv vllm-env  # you can use "uv venv vllm-env" alternatively, if you have uv installed
source vllm-env/bin/activate  # On Windows use "vllm-env\Scripts\activate"
pip install vllm  # use "uv pip install vllm" if your environment installed by uv
python -m vllm.entrypoints.openai.api_server \
--model Qwen/Qwen2-1.5B-Instruct \
--trust-remote-code \
--dtype half
