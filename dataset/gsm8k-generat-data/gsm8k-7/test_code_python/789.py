def solution():
    num_days_to_fully_heal = 3 * 5
    num_days_to_rest_after_healing = 3
    num_weeks_to_wait_to_start_lifting = 3

    # Calculate the total number of days from injury to starting heavy lifting again
    total_days = num_days_to_fully_heal + num_days_to_rest_after_healing + (num_weeks_to_wait_to_start_lifting * 7)

    result = total_days
    return result

print(solution())