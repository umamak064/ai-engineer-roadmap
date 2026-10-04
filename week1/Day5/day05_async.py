import httpx
import asyncio
import time
async def task1():
    await asyncio.sleep(4)
    return "task1 done"

async def task2():
    await asyncio.sleep(2)
    return "task2 done"

async def main():
    result=await asyncio.gather(
        task1(),
        task2()
    )
    print(result)
asyncio.run(main())    

# PRACTICE
# 1. Write an async function slow_task(name, seconds) that does await asyncio.sleep(seconds) then prints f"
# {name} done" .

async def slow_task(name,seconds):
    await asyncio.sleep(seconds)
    return f"{name} done"


# 2. Run 3 slow_task calls one after another with await (sequential) — time it.

async def seq_result():
    start=time.time()
    result1=await slow_task("umama",5)
    print (result1)
    result2=await slow_task("sara",9)
    print(result2)
    result3=await slow_task("hina",2)
    print(result3)
    print(time.time() - start)

asyncio.run(seq_result())  
 

    
    



# 3. Run the same 3 calls with asyncio.gather() (concurrent) — time it. Compare.

async def main():
    start=time.time()
    result=await asyncio.gather(
        slow_task("umama",5),
        slow_task("sara",9),
        slow_task("hina",2)
    )
    print(result)
    print(time.time() - start)

asyncio.run(main())    
    
# 4. Write an async function using httpx.AsyncClient() to fetch one real URL (e.g., a placeholder JSON API)
# and print the status code.

async def fetch_url():
    async with httpx.AsyncClient() as Client:
        response=await Client.get("https://jsonplaceholder.typicode.com/todos/1")
        print(response.status_code)
        print(response.json())
asyncio.run(fetch_url())
        



    
