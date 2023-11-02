def solution():
    
    total_cost = 45
    black_notebook_cost = 15
    pink_notebook_cost = 10
    green_notebooks_cost = (total_cost - black_notebook_cost - pink_notebook_cost) / 2
    result = green_notebooks_cost
    return result

print(solution())