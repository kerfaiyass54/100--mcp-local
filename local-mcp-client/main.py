import asyncio

from llama_index.tools.mcp import BasicMCPClient, McpToolSpec
from llama_index.core.workflow import Context

from agent import get_agent
from interaction import handle_user_message


async def main():

    # Connect to MCP server
    mcp_client = BasicMCPClient(
        "http://127.0.0.1:8000/sse"
    )

    # Load MCP tools
    mcp_tool = McpToolSpec(client=mcp_client)

    # Create agent
    agent = await get_agent(mcp_tool)

    # Shared memory
    agent_context = Context(agent)

    print("MCP Agent Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your message: ")

        if user_input.lower() == "exit":
            break

        print("User:", user_input)

        response = await handle_user_message(
            user_input,
            agent,
            agent_context,
            verbose=True
        )

        print("Agent:", response)
        print()


if __name__ == "__main__":
    asyncio.run(main())