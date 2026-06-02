from llama_index.tools.mcp import McpToolSpec
from llama_index.core.agent.workflow import FunctionAgent

from ollama_client import llm
from prompts import SYSTEM_PROMPT


async def get_agent(mcp_tools: McpToolSpec):
    tools = await mcp_tools.to_tool_list_async()

    agent = FunctionAgent(
        name="DatabaseAgent",
        description="Agent that interacts with PostgreSQL through MCP tools.",
        tools=tools,
        llm=llm,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent