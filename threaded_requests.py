from threading import Thread
from time import perf_counter, sleep


def response() -> str:
    """Simulates a response from an I/O bound task.

    Returns:
        Information regarding the packet requested.
    """

    sleep(1)
    return "packet example abc"


def request_packet() -> str:
    """Simulates a request for some data that is I/O bound.

    Returns:
        A confirmation that the data has been received.
    """

    packet = response()
    print(packet)


def spawn_requests(amount: int) -> None:
    """Spawns the specified number of requests in 'amount'

    Arguments:
        amount (int): The number of requests to run.
    """

    requests = []

    # Spawns threads to send requests.
    for _ in range(amount):
        thread = Thread(target=request_packet)
        thread.start()
        requests.append(thread)

    for request in requests:
        request.join()


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
    spawn_requests(amount)

    end = perf_counter()
    print("end")

    return end - start


def main() -> None:
    amount = 1000
    time_taken = time_requests(amount)
    print(f"""\nCompleted {amount} requests in {time_taken:.4f} seconds""")


if __name__ == "__main__":
    main()
