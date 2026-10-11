
from mcp.server.mcpserver import MCPServer
mcp = MCPServer("SRE MCP Server")

@mcp.tool()
def greeting(name:str) -> str:
    "send a greeting"
    return f"Hi {name}, I am your SRE assistant, what can I help you?"

@mcp.tool()
def gatherinformation(name:str) -> str:
    "passive and active information gathering"
    return f"Gathering information ... "
@mcp.tool()
def portscanning(name:str) -> str:
    "port scanning and vulnerability analysis"
    return f"Port scanning and doing vulnerability analysis ... "

@mcp.tool()
def exploitation(name:str) -> str:
    "Exploitation, trying to gain access"
    return f"Doing exploitation,trying hard to gain access... "
@mcp.tool()
def generatereport(name:str) -> str:
    "Generate pentest report"
    return f"Generating pentest report ... "

@mcp.tool()
def sendreport(name:str) -> str:
    "email pentest report"
    return f"Sending pentest report to you ... "

@mcp.tool()
def cleanup(name:str) -> str:
    "cleanup the test enviornment"
    return f"Cleaning up the test enviornment, thanks for your patient ... "

if __name__ == "__main__":
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8084)