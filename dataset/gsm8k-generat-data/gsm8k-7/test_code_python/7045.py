def solution():
    vacuuming_time = 2  # hours
    dishwashing_time = 0.5  # hours
    bathroom_cleaning_time = 3 * dishwashing_time  # hours

    # Calculate the total time spent on chores
    total_time = vacuuming_time * 2 + dishwashing_time + bathroom_cleaning_time

    # Calculate the total earning from the chores
    earning = total_time * 5

    result = earning
    return result

print(solution())