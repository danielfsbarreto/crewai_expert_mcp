from typing import Any

import dotenv
from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import Response

from services import CrewaiEnterpriseService

dotenv.load_dotenv()
mcp = FastMCP("CrewAI Expert")


@mcp.custom_route("/", methods=["HEAD"])
async def head_root(request: Request) -> Response:
    """HEAD endpoint for the root path returning a valid response."""
    return Response(
        status_code=200,
        headers={
            "Content-Type": "application/json",
            "Server": "CrewAI Expert MCP Server",
            "X-MCP-Server": "CrewAI Expert",
        },
    )


@mcp.tool()
def answer_crewai_question(question: str) -> dict[str, Any]:
    """Answer a CrewAI question through an automation living in CrewAI Enterprise.

    Args:
        prompt: The CrewAI-related question to be answered

    Returns:
        dict: A dictionary with a "final_answer" key containing the response to the user's question.
    """
    return CrewaiEnterpriseService().call(question)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
