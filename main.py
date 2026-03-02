"""Simple module containing a recursive Fibonacci implementation."""


def fib(n: int) -> int:
    """Return the nth Fibonacci number using recursion.

    The sequence is defined as::

        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2)  for n > 1

    This implementation is intentionally naive for educational purposes.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # quick demonstration when run as a script
    import sys

    try:
        arg = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Please provide an integer argument")
        sys.exit(1)

    print(f"fib({arg}) = {fib(arg)}")
