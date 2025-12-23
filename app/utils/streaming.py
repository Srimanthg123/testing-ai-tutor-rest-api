from sse_starlette.sse import EventSourceResponse

def stream_response(generator):
    async def event_generator():
        async for chunk in generator:
            yield {"data": chunk}

    return EventSourceResponse(event_generator())