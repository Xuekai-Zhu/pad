def solution():
    # Define the time Tim spends meditating and reading per day
    meditate_time = 1
    read_time = 2 * meditate_time

    # Calculate the time Tim spends reading per week
    read_time_per_week = read_time * 7
    result = read_time_per_week
    return result

print(solution())