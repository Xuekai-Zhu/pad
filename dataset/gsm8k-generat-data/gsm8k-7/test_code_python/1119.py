def solution():
    num_days = 5
    first_day_time = 5

    # Calculate the total amount of time spent talking each day
    daily_times = [first_day_time * 2**i for i in range(num_days)]

    # Calculate the total amount of time spent talking for the week
    total_time = sum(daily_times)
    result = total_time
    return result

print(solution())