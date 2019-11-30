from typing import Generator
from random import randint
import time
import asyncio


def odds(start, end) -> Generator:
    """
    Produce a sequence of odd values starting from start until end including end
    Args:
        start:
        end:

    Returns: Yield each value

    """

    for odd in range(start, end + 1, 2):
        yield odd


def randn_synchronous_version():
    time.sleep(3)
    return randint(1, 10)


async def randn():
    await asyncio.sleep(3)
    return randint(1, 10)


async def square_odds(start, stop):
    for odd in odds(start, stop):
        await asyncio.sleep(2)  # This is what makes this function asynchronous, we are pretending that we are
        # talking to a database or a webserver or a file system
        yield odd ** 2   # Because we want a generator


async def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    # print(odd_values)
    # print(odds2)

    start = time.perf_counter()
    r = await randn()
    elapsed = time.perf_counter() - start
    print(f'{r} took {elapsed:0.2f} seconds.')

    start = time.perf_counter()
    r = await asyncio.gather(*[randn() for _ in range(10)])
    elapsed = time.perf_counter() - start
    print(f'{r} took {elapsed:0.2f} seconds.')

    # Normally for a generator you'd use for..in loop, because this is an async generator, you'd use async for..in loop
    async for so in square_odds(11, 17):
        print(f'so is {so}')


if __name__ == "__main__":
    asyncio.run(main())     # this creates the event loop for our async tasks
