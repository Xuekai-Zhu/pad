def solution():
    spent_per_sibling = 30
    num_siblings = 3
    total_spent = 150

    # Calculate the total amount spent on siblings
    total_spent_on_siblings = spent_per_sibling * num_siblings

    # Calculate the amount spent on parents
    spent_on_parents = total_spent - total_spent_on_siblings

    # Divide the amount spent on parents equally for each parent
    spent_per_parent = spent_on_parents / 2
    result = spent_per_parent
    return result

print(solution())