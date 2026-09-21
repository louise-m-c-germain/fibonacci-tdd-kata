import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return (pytest,)


@app.function
def fibonacci(n):
    """ Return the n-th fibonacci number
        Reminder: the Fibonacci sequence is defined by  F(0) = 0d  F(1) = 1   F(n) = F(n−1) + F(n−2)    for n ≥ 2
        """
    if n==0 :
        return(0)
    elif n==1 :
        return(1)
    else : 
        return(fibonacci(n-1)+fibonacci(n-2))


@app.cell
def _(pytest):
    #List of test to pass

    @pytest.mark.parametrize("n,expected",[(0,0),(1,1),(2,1),(6,8),(10,55)])

    def test_fibonacci(n,expected):
        assert fibonacci(n)==expected


    return


if __name__ == "__main__":
    app.run()
