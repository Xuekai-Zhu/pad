def solution():
    
    initial_notebooks = 10
    notebooks_ordered = 6
    notebooks_lost = 2
    total_notebooks = initial_notebooks + notebooks_ordered - notebooks_lost
    result = total_notebooks
    return result

print(solution())