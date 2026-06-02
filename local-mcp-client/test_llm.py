# test_llm.py

from ollama_client import llm

response = llm.complete(
    "Explain MCP in one sentence."
)

print(response)