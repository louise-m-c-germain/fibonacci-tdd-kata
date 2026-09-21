import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return


@app.function
def fibonacci(n):
    """ Return the n-th fibonacci number
        Reminder: the Fibonacci sequence is defined by  F(0) = 0d  F(1) = 1   F(n) = F(n−1) + F(n−2)    for n ≥ 2
        """


if __name__ == "__main__":
    app.run()
