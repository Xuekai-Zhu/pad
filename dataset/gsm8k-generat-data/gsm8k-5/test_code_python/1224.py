def solution():
    # Calculate the value of Jim's portfolio after the first year
    first_year_gain = 0.15 * 80  # Jim's portfolio grows by 15%
    first_year_total = 80 + first_year_gain  # Jim's portfolio after one year
    # Calculate the total value of Jim's portfolio after the second year
    second_year_gain = 0.10 * (first_year_total + 28)  # Jim's portfolio grows by 10% after adding $28
    total_value = first_year_total + 28 + second_year_gain  # Jim's final portfolio worth after 2 years
    result = total_value
    return result

print(solution())