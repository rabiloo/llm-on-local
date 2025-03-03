curl -X POST http://localhost:11434/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{
          "model": "llama3.2:1b",
          "messages": [{"role": "user", "content": "Explain recursion in simple terms."}],
          "temperature": 0.2
        }'