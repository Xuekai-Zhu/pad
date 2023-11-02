def solution():
    """The educational shop is selling notebooks for $1.50 each and a ballpen at $0.50 each. William bought five notebooks and a ballpen. How much did he spend in all?"""
    notebook_price = 1.5
    ballpen_price = 0.5
    num_notebooks = 5
    num_ballpens = 1
    total_cost = (notebook_price * num_notebooks) + (ballpen_price * num_ballpens)
    result = total_cost
    return result

print(solution())