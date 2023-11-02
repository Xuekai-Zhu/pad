def solution():
    # Define the number of shots blocked in each period
    first_period = 4
    second_period = 2 * first_period
    third_period = second_period - 3

    # Calculate the total number of shots blocked in the first three periods
    total_shots_first_three_periods = first_period + second_period + third_period

    # Calculate the number of shots blocked in the fourth period
    fourth_period = 21 - total_shots_first_three_periods
    result = fourth_period
    return result

print(solution())