curl -fsSL https://ollama.com/install.sh | sh
ollama serve &>/dev/null &
ollama --version
ollama pull llama3.2:1b

# Chat with model directly
#ollama run llama3.2:1b

# Delete model
#ollama rm llama3.2:1b

# Stop Ollama
#pkill ollama
