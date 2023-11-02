def solution():
    # Calculate the number of minutes needed to heat the dish to 100 degrees
    current_temp = 20
    desired_temp = 100
    increase_per_minute = 5
    time_needed = (desired_temp - current_temp) / increase_per_minute
    result = time_needed
    return result

print(solution())