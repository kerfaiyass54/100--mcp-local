from mcp.server.fastmcp import FastMCP

from db import get_connection

mcp = FastMCP("postgres-demo")


@mcp.tool()
def add_data(content: str) -> bool:
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO notes(content) VALUES (%s)",
                (content,),
            )

        conn.commit()
        return True

    finally:
        conn.close()


@mcp.tool()
def fetch_data(limit: int = 10) -> list:
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, content, created_at
                FROM notes
                ORDER BY id DESC
                LIMIT %s
                """,
                (limit,),
            )

            rows = cur.fetchall()

        return [
            {
                "id": r[0],
                "content": r[1],
                "created_at": str(r[2]),
            }
            for r in rows
        ]

    finally:
        conn.close()


if __name__ == "__main__":
    print("Starting PostgreSQL MCP Server...")
    mcp.run()