def solution():
    # Calculate the total number of apples eaten by the children
    children_apples = 33 * 10

    # Calculate the remaining apples for the adults
    adult_apples = 450 - children_apples

    # Calculate the number of adults in the family
    num_adults = adult_apples // 3

    result = num_adults
    return result

print(solution())