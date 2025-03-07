# Fewest Scripts, Maximum Power: Serve LLMs Locally with Ollama  

Here is the repository that contains the demo scripts of this [Rabiloo blog post](https://rabiloo.com/blog/fewest-scripts-maximum-power-serve-llms-locally-with-ollama).

We are going to follow the instructions below to set up the environment and serve LLMs locally.

## Prerequisites
- Bash: A Unix-like shell (Linux/macOS). Windows users can use Git Bash or WSL.
- Python: Python 3.8 or higher installed. You can download it from [Python download link](https://www.python.org/downloads/).

## Run Scripts

First, we should install Ollama, get the models we want to use, then run them.

```bash
cd ollama/scripts
bash get_started.sh
```

Now we have Ollama served our local computer. You can read the ```get_started.sh``` file or the blog post for more information.

### Curl Example

If using ```curl```, we just run this command:

```bash
curl -X POST http://localhost:11434/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{
          "model": "your_model",
          "messages": [{"role": "user", "content": "Your question"}],
          "temperature": 0.2
        }'
```

```your_model``` is the alias of the LLM, you can find it in this [Ollama library](https://ollama.com/library).

```content``` is your question that you want to ask the LLM.

```temparature``` controls randomness (higher = more creative, lower = more deterministic).

Or you can update the configuration in curl.sh, then run:

```bash
bash curl.sh
```

### Python Example
#### Create a Virtual Environment
We highly recommend using a virtual environment to manage dependencies. You can use either Python’s built-in venv or a tool like conda.

- Using venv (recommended):
```bash
cd ollama

# Create a virtual environment named 'venv'
python -m venv chatbot

# Activate the virtual environment:
# On Linux/macOS:
source chatbot/bin/activate
# On Windows:
chatbot\Scripts\activate
```
- Using conda:

You can use Miniconda - the small version of Conda:
  
```bash
# Install and activate miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p miniconda3
source miniconda3/bin/activate

# Create a conda environment named 'chatbot' with Python 3.10
conda create -n chatbot python=3.10 -y

# Activate the environment
conda activate chatbot

```

#### FastAPI
Run the command:

```bash
bash scripts/fastapi.sh
```

The app will be available at http://127.0.0.1:8000, and we can try it with Swagger UI at http://127.0.0.1:8000/docs.

Stop the app: Press ```Ctrl+C```

#### Gradio
Run the command:

```bash
bash scripts/gradio.sh
```

You can try the gradio app at:
- local URL http://0.0.0.0:7860
- public URL: https://xxxxxxxxxxxxxxxxxx.gradio.live

(URLs will be shown in the logging)

Stop the app: Press ```Ctrl+C```

## References
- [Ollama](https://ollama.com/)

## Contact
If you have any questions, or you want to collaborate with us, please feel free to contact us via https://rabiloo.com/contact-us.
