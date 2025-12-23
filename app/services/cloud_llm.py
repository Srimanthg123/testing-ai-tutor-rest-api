import asyncio

async def gemini_generate(prompt: str):
    response = "Streaming response from Gemini cloud model."
    for word in response.split():
        await asyncio.sleep(0.2)
        yield word + " "