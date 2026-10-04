import httpx
import asyncio
import time

#  BUILD
# Build: A concurrent URL fetcher. What it should do: A function fetch_all(urls: list[str]) that fetches all
# URLs concurrently using httpx.AsyncClient() and asyncio.gather() , and returns a list of results. Test with 5
# URLs and print total time taken vs. what sequential would have taken. 

# CHALLENGE
# Modify fetch_all so that if ONE url fails (times out or errors), the whole function doesn’t crash — it should
# return the successful results plus a clear note about which URL(s) failed. Try for 20–30 minutes before
# looking anything up.


async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        try:
           result= await client.get(url)
           return result
        except Exception as e:
            return f"FAILED: {url} - {e}"

async def main(urls:list[str]):
        start=time.time()
        result=await asyncio.gather(
            *[fetch_url(url) for url in urls]
        
        )
        print(result)
        print(time.time()-start)

async def sequential_main(urls:list[str]):
        start=time.time()
        results=[]
        for url in urls:
            result= await fetch_url(url)
            results.append(result)

        print(results)
        print(time.time()-start)        

asyncio.run(main(["https://jsonplaceholder.typicode.com/todos/1","https://this-url-does-not-exist-12345.com",
           "https://jsonplaceholder.typicode.com/users/1","https://jsonplaceholder.typicode.com/posts/1",
           "https://jsonplaceholder.typicode.com/comments/1"]))


asyncio.run(sequential_main(["https://jsonplaceholder.typicode.com/todos/1","https://this-url-does-not-exist-12345.com",
           "https://jsonplaceholder.typicode.com/users/1","https://jsonplaceholder.typicode.com/posts/1",
           "https://jsonplaceholder.typicode.com/comments/1"]))









      
        



