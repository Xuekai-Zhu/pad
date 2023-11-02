def solution():
    # Calculate the gap between the older brother and older sister
    brother_sister_gap = 1936 - 1932

    # Calculate the gap between the grandma and her sister
    grandma_sister_gap = 2 * brother_sister_gap

    # Calculate the year of the grandma's birth
    grandma_birth_year = 1936 + grandma_sister_gap

    result = grandma_birth_year
    return result

print(solution())