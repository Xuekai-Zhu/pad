def solution():
    recovery_time = 3  # It took James 3 days for the pain to subside
    full_healing_time = recovery_time * 5  # It takes at least 5 times recovery time for the injury to fully heal
    waiting_time = 3  # James wants to wait another 3 days after the injury is fully healed before working out again
    total_wait_time = recovery_time + full_healing_time + waiting_time  # Total time James needs to wait before lifting heavy again
    weeks_in_days = 7  # There are 7 days in a week

    # Calculate the number of weeks James needs to wait before lifting heavy again
    waiting_weeks = 3
    total_weeks = (total_wait_time + waiting_weeks) / weeks_in_days
    result = round(total_weeks, 2)
    return result

print(solution())