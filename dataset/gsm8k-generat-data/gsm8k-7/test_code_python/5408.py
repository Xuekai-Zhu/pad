def solution():
    num_peanuts_per_15_seconds = 20
    num_seconds_per_minute = 60
    num_minutes = 6

    # Calculate the total number of 15-second intervals in 6 minutes
    num_intervals = num_minutes * (num_seconds_per_minute // 15)

    # Calculate the total number of peanuts Darma can eat in 6 minutes
    total_peanuts = num_intervals * num_peanuts_per_15_seconds
    result = total_peanuts
    return result

print(solution())