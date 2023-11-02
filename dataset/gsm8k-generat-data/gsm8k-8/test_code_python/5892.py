def solution():
    # Calculate the number of adult men
    adult_men = 0.3 * 2000

    # Calculate the number of adult women
    adult_women = 2 * adult_men

    # Calculate the number of children
    children = 2000 - adult_men - adult_women

    result = children
    return result

print(solution())