from asyncio import create_task, sleep, run
from time import perf_counter


async def response() -> str:
    """Simulates a response from an I/O bound task.

    Returns:
        Information regarding the packet requested.
    """

    await sleep(1)
    return "packet example abc"


async def request_packet() -> None:
    """Simulates a request for some data that is I/O bound."""

    packet = await response()
    print(packet)


async def spawn_requests(amount: int) -> None:
    """Spawns the specified number of requests in 'amount'

    Arguments:
        amount (int): The number of requests to run.
    """

    requests = []

    # Spawns coroutines to send requests.
    for _ in range(amount):
        task = create_task(request_packet())
        requests.append(task)

    for request in requests:
        await request


def time_requests(amount: int) -> float:
    """Times how long the specified number of requests takes.

    Arguments:
        amount (int): The number of requests to to time.

    Returns:
        The time it takes to process all requests.
    """

    print("start")
    start = perf_counter()

    # Starts sending requests
    run(spawn_requests(amount))

    end = perf_counter()
    print("end")

    return end - start


def main() -> None:
    amount = 1000
    time_taken = time_requests(amount)
    print(f"""\nCompleted {amount} requests in {time_taken:.4f} seconds""")


if __name__ == "__main__":
    main()
