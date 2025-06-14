from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()
# Create a FastMCP instance
mcp = FastMCP(
    name="Veronica",
    host="0.0.0.0",
    port=8060
)

# Tools
@mcp.tool()
def fetch_data(query: str):
    # Your data fetching code here
    pass

@mcp.tool()
def whatsapp_notifications():
    # Your WhatsApp API code here
    pass

@mcp.tool()
def whatsapp_messenger():
    # Your WhatsApp API code here
    pass

@mcp.tool()
def instagram_notifications():
    # Your Instagram API code here
    pass

@mcp.tool()
def instagram_messenger():
    # Your Instagram API code here
    pass

# Run the server
if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")