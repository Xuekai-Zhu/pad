def solution():
    
    number_of_children = 3
    john_notebooks_per_child = 2
    john_total_notebooks = john_notebooks_per_child * number_of_children
    wife_notebooks_per_child = 5
    wife_total_notebooks = wife_notebooks_per_child * number_of_children
    total_notebooks = john_total_notebooks + wife_total_notebooks
    result = total_notebooks
    return result

print(solution())