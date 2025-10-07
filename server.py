from typing import Any

import dotenv
from mcp.server.fastmcp import FastMCP

from services import CrewaiEnterpriseService

dotenv.load_dotenv()
mcp = FastMCP("CrewAI Expert")


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
