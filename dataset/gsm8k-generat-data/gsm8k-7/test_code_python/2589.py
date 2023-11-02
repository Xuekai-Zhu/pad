def solution():
    total_apples = 450
    num_children = 33
    child_apples = 10

    # Calculate the total number of apples eaten by children
    children_apples_total = num_children * child_apples

    # Calculate the total number of apples eaten by adults
    adult_apples_total = total_apples - children_apples_total

    # Calculate the number of adults in the family
    num_adults = adult_apples_total // 3
    result = num_adults
    return result

print(solution())