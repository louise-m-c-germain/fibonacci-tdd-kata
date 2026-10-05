def fibonacci(n: int, f0: int = 0, f1: int = 1) -> int:
    """
    Efficiently compute the nth Fibonacci number using matrix exponentiation.

    The tuple (a, b) represents a matrix of the form [[a + b, a], [a, b]].
    It is initialized to the identity matrix [[1, 0], [0, 1]]. The matrix is
    squared repeatedly, and multiplied by the matrix [[1, 1], [1, 0]] if the
    current bit of n is 1.

    Once the loop is done, the produced matrix corresponds to [[1, 1], [1, 0]]
    to the power of n. Multiplying it by the vector [F(1), F(0)] gives the
    vector [F(n+1), F(n)]. The Fibonacci number F(n) is then returned.
    """
    a, b = 0, 1
    for bit in f"{n:b}":
        a, b = (a + 2 * b) * a, a * a + b * b
        if bit == "1":
            a, b = a + b, a
    return a * f1 + b * f0
