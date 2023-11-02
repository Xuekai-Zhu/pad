def solution():
    # Apples produced in first year
    year_one = 40

    # Apples produced in second year
    year_two = (2 * year_one) + 8

    # Apples produced in third year
    year_three = int(year_two * (3/4))

    # Total apples produced in first three years
    total_apples = year_one + year_two + year_three

    result = total_apples
    return result

print(solution())