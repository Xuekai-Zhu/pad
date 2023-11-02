def solution():
    # Calculate the length of the trial
    trial_length = 4 * 2

    # Calculate the number of hours spent in deliberation
    deliberation_hours = 6 * 24

    # Calculate the total time spent on jury duty in hours
    total_hours = 2 * 24 + trial_length * 24 + deliberation_hours

    # Calculate the total number of days spent on jury duty
    total_days = total_hours / 16

    result = total_days
    return result

print(solution())