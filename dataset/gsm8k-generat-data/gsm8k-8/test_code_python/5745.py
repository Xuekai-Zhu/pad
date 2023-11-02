def solution():
    # Calculate the total number of minutes in 2 hours
    total_minutes = 2 * 60

    # Calculate the duration of one cycle (standing and sitting)
    cycle_duration = 10 + 5

    # Calculate the number of cycles that can be completed in the total time
    cycles_completed = total_minutes // cycle_duration

    result = cycles_completed
    return result

print(solution())