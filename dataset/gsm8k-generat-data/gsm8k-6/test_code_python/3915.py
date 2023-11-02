def solution():
    # Calculate the total number of shots blocked in the first three periods
    first_period_shots = 4
    second_period_shots = 2 * first_period_shots
    third_period_shots = second_period_shots - 3
    total_shots = first_period_shots + second_period_shots + third_period_shots

    # Calculate the number of shots blocked in the fourth period
    fourth_period_shots = 21 - total_shots
    result = fourth_period_shots
    return result

print(solution())