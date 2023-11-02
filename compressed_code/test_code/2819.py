def solution():
    
    total_notebooks = 12
    total_cost = 37
    red_notebooks = 3
    green_notebooks = 2
    red_cost = 4
    green_cost = 2
    blue_cost = (total_cost - red_notebooks * red_cost - green_notebooks * green_cost) / (total_notebooks - red_notebooks - green_notebooks)
    result = blue_cost
    return result

print(solution())