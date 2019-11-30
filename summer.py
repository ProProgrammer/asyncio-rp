"""
A Real world application of what we studied so far regarding co-routines, asynchronous generators, etc.
We will call a http API returning JSON object
API URL: http://qrng.anu.edu.au/API/jsonI.php?length=10&type=uint16
    This returns list of random integers of type uint16 of length 10
"""

import asyncio
import json
import time

import aiohttp  # Python package that allows asynchronous (non-blocking) http fetches - pip install aiohttp


async def worker(name, n, session):
    print(f'worker-{name}')
    url = f'http://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16'
    response = await session.request(method='GET', url=url)     # Actual statement that sends the request out to
    # internet
    value = await response.text()
    value = json.loads(value)
    return sum(value['data'])       # This is why this program is called 'summer.py' - It returns sym of values


async def main():
    # Create a http session
    # send it off to a worker task
    async with aiohttp.ClientSession() as session:
        response = await worker('bob', 3, session)
        print(f'response is {response}. type: {type(response)}')
    # await asyncio.sleep(1)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'Executed in {elapsed:0.2f} seconds.')
