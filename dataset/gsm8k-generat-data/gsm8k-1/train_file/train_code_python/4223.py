def solution():
    """Peter bought 4 new notebooks for school. 2 of them are green, one is black and the other one is pink. The total cost was $45. If the black notebook cost $15, and the pink one cost $10, how much did the green notebooks cost each?"""
    total_cost = 45
    black_notebook_cost = 15
    pink_notebook_cost = 10
    green_notebooks_cost = (total_cost - black_notebook_cost - pink_notebook_cost) / 2
    result = green_notebooks_cost
    return result

print(solution())