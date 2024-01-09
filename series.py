# series.py

def fibonacci(n):
    """Generate the nth value in the Fibonacci series."""
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[n - 1] if n > 0 else None

def lucas(n):
    """Generate the nth value in the Lucas numbers."""
    lucas_series = [2, 1]
    while len(lucas_series) < n:
        lucas_series.append(lucas_series[-1] + lucas_series[-2])
    return lucas_series[n - 1] if n > 0 else None

def sum_series(n, first=0, second=1):
    """
    Generate the nth value in a series based on the first and second values.

    If first and second are not provided, the function produces Fibonacci series.
    If first=2 and second=1, the function produces Lucas numbers.
    Other values for first and second will produce other series.
    """
    series = [first, second]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[n - 1] if n > 0 else None