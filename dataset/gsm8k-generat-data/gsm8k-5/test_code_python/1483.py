def solution():
    siblings_spending = 30 * 3  # Mia spent $30 on each of her 3 siblings
    parents_spending = 150 - siblings_spending  # Mia spent the rest of her money on her parents
    number_of_parents = 2  # Mia has 2 parents

    # Calculate the spending on each parent's gift
    parent_spending = parents_spending / number_of_parents
    result = parent_spending
    return result

print(solution())