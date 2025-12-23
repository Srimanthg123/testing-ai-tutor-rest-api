import time

def local_generate(prompt: str, stream: bool = False):
    response = f"Local AI personalized response for: {prompt}"

    if not stream:
        return response

    def generator():
        for word in response.split():
            yield word + " "
            time.sleep(0.2)

    return generator()