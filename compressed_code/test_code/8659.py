def solution():
    
    total_cost = 37
    total_notebooks = 12
    red_notebooks = 3
    green_notebooks = 2
    blue_notebooks = total_notebooks - red_notebooks - green_notebooks
    
    red_cost = red_notebooks * 4
    green_cost = green_notebooks * 2
    blue_cost = total_cost - red_cost - green_cost
    
    cost_per_blue_notebook = blue_cost / blue_notebooks
    result = cost_per_blue_notebook
    return result

print(solution())