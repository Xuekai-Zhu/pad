def solution():
    first_exp_weeks = 3
    second_exp_weeks = first_exp_weeks + 2
    third_exp_weeks = second_exp_weeks * 2

    # Calculate the total number of weeks spent on all expeditions
    total_weeks = first_exp_weeks + second_exp_weeks + third_exp_weeks

    # Calculate the total number of days spent on the island
    total_days = total_weeks * 7
    result = total_days
    return result

print(solution())