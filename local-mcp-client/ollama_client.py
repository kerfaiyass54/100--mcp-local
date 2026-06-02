from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

SYSTEM_PROMPT = """
You are an AI assistant with access to external tools through MCP.

Always use available tools when needed.
Never make up database information.
Use tools before answering database-related questions.
"""

llm = Ollama(
    model="deepseek-r1:7b",
    request_timeout=120.0,
    system_prompt=SYSTEM_PROMPT,
)

Settings.llm = llm