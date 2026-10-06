# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "fibonacci-kata-lgermain",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci


@app.cell
def _():
    mo.md(r"""
    # Fibonacci Explorer

    Pick a range below and see the Fibonacci numbers it contains,
    both as a list and as a chart of their growth. This notebook
    consumes the published fibonacci_kata package — it does not
    reimplement the function.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(0, 50, value=0, label="Range start")
    end = mo.ui.slider(0, 50, value=20, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    indices = list(range(lo, hi + 1))
    results = [fibonacci(n) for n in indices]
    results
    return indices, results


@app.cell
def _(indices, results):
    fig, ax = plt.subplots()
    ax.plot(indices, results, marker="o", color="#4c72b0")
    ax.set_xlabel("n")
    ax.set_ylabel("F(n)")
    ax.set_yscale("log")
    ax.set_title("Growth of the Fibonacci sequence over the selected range")
    fig
    return


if __name__ == "__main__":
    app.run()
