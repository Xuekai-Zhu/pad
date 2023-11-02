def solution():
    # Calculate the total number of apples produced in the first three years
    year_1 = 40
    year_2 = (2 * year_1) + 8
    year_3 = (3/4) * year_2
    total_apples = year_1 + year_2 + year_3
    result = total_apples
    return result

print(solution())