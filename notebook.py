import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return mo, pytest


@app.function
#Code find on the website Stack Overflow 

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


@app.cell
def _(pytest):
    #List of tests to pass

    @pytest.mark.parametrize("n,expected",[(0,0),(1,1),(2,1),(6,8),(10,55)])

    def test_fibonacci(n,expected):
        assert fibonacci(n)==expected


    return


@app.cell
def _(mo):
    #Widget
    n_slider = mo.ui.slider(0,50)
    n_slider
    return (n_slider,)


@app.cell
def _(mo, n_slider):
    mo.md(f"F({n_slider.value}) = {fibonacci(n_slider.value)}")
    return


@app.cell
def _(pytest):
    #Aditional unit test for large value

    @pytest.mark.parametrize("n",[1000,10**4,10**5,10**6,10**7])

    def test_fibonacci_huge_numbers(n):
        assert fibonacci(n) > 0

    return


if __name__ == "__main__":
    app.run()
