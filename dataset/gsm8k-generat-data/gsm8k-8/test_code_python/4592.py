def solution():
    # Define the number of weeks spent on each expedition
    first_exp = 3
    second_exp = first_exp + 2
    third_exp = 2 * second_exp

    # Calculate the total number of weeks spent on the island
    total_weeks = first_exp + second_exp + third_exp

    # Calculate the total number of days spent on the island
    total_days = total_weeks * 7
    result = total_days
    return result

print(solution())