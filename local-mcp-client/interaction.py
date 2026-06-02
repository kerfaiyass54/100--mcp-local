from llama_index.core.agent.workflow import (
    FunctionAgent,
    ToolCall,
    ToolCallResult,
)

from llama_index.core.workflow import Context


async def handle_user_message(
    message_content: str,
    agent: FunctionAgent,
    agent_context: Context,
    verbose: bool = False,
) -> str:

    handler = agent.run(
        message_content,
        ctx=agent_context,
    )

    async for event in handler.stream_events():

        if isinstance(event, ToolCall):
            print(f"Calling tool: {event.tool_name}")

        elif isinstance(event, ToolCallResult):

            if verbose:
                print(
                    f"Tool {event.tool_name} returned:"
                )
                print(event.tool_output)

    response = await handler

    return str(response)