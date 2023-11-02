def solution():
    
    children = 3
    john_notebooks_per_child = 2
    wife_notebooks_per_child = 5
    john_total_notebooks = children * john_notebooks_per_child
    wife_total_notebooks = children * wife_notebooks_per_child
    total_notebooks = john_total_notebooks + wife_total_notebooks
    result = total_notebooks
    return result

print(solution())