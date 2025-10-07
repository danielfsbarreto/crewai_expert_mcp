# CrewAI Enterprise MCP Server

# Installation:
1. pip install uv if you don't have it
2. uv lock
3. uv sync

## Overview

A Model Context Protocol (MCP) server implementation that provides deployed CrewAI workflows. This server enables kicking off your deployed crew and inspect the status giving the results of your crew.

## Tools

- kickoff_crew
- get_crew_status

## Env Variables

### Retrieve from app.crewai.com
`MCP_CREWAI_ENTERPRISE_SERVER_URL` = "https://crewai-expert-aa6791ac-f605-4a9f-b19a-74f8b-ccef7330.crewai.com"
`MCP_CREWAI_ENTERPRISE_BEARER_TOKEN` = "ae1387522f4b"

# Usage with Claude Desktop

To use this MCP server with Claude Desktop, follow these steps:

1. Open Claude Desktop
2. Go to Settings > Developer Settings
3. Add a new MCP server with the configuration shown below

## Locally, cloned repo:

Install `mcp` and `mcp[cli]` locally

```json
{
"mcpServers": {
    "crewai_enterprise_server": {
    "command": "uv",
    "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "<DOWNLOADED_MCP_SERVER_PATH>/crewai_enterprise_server.py",
    ],
    "env": {
        "MCP_CREWAI_ENTERPRISE_SERVER_URL": "https://crewai-expert-aa6791ac-f605-4a9f-b19a-74f8b-ccef7330.crewai.com",
        "MCP_CREWAI_ENTERPRISE_BEARER_TOKEN": "ae1387522f4b"
    }
    }
}
}
```
