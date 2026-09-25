import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return mo, pytest


@app.function
#definition of the function fibonacci
#version with no recursive function

def fibonacci(n):
    """ Return the n-th fibonacci number
        Reminder: the Fibonacci sequence is defined by  F(0) = 0d  F(1) = 1   F(n) = F(n−1) + F(n−2)    for n ≥ 2
        """
    a,b = 0,1
    for i in range(n):  
        a,b = b,a+b
    return(a)


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


if __name__ == "__main__":
    app.run()
