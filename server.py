
from mcp.server.mcpserver import MCPServer
mcp = MCPServer("SRE MCP Server")

@mcp.tool()
def greeting(name:str) -> str:
    "send a greeting"
    return f"Hi {name}, I am your SRE assistant, what can I help you?"

if __name__ == "__main__":
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8084)