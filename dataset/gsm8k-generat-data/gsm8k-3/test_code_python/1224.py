def solution():
    """Jim starts with $80 in his investment portfolio. After 1 year it grows by 15%. He then adds another $28 to his portfolio. After 1 more year the combined portfolio grows by 10%. What is his final portfolio worth after 2 years from when he started?"""
    
    # Calculate the value of Jim's portfolio after the first year
    year_one_growth = 0.15
    year_one_value = 80 + (80 * year_one_growth)

    # Calculate the value of Jim's portfolio after adding $28
    year_two_start_value = year_one_value + 28

    # Calculate the value of Jim's portfolio after the second year
    year_two_growth = 0.10
    year_two_value = year_two_start_value + (year_two_start_value * year_two_growth)

    # Display Jim's final portfolio value
    result = year_two_value
    return result

print(solution())