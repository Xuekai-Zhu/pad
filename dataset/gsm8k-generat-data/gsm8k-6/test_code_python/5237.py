def solution():
    # Calculate the total distance Wanda walks in one day
    daily_distance = 0.5*2  # Wanda walks a total of 0.5 miles to school and 0.5 miles back home
    weekly_distance = daily_distance * 5  # Wanda walks this distance 5 days a week
    total_distance = weekly_distance * 4  # Wanda walks this distance for 4 weeks
    result = total_distance
    return result

print(solution())