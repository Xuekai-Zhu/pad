def solution():
    # Calculate the value of Jim's portfolio after one year of growth
    year_one_growth = 0.15 * 80
    year_one_total = 80 + year_one_growth

    # Calculate the value of Jim's portfolio after the additional $28 is added
    year_one_total += 28

    # Calculate the value of Jim's portfolio after two years of growth
    year_two_growth = 0.10 * year_one_total
    year_two_total = year_one_total + year_two_growth

    result = year_two_total
    return result

print(solution())