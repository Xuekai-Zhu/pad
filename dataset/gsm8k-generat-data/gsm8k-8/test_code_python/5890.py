def solution():
    # Calculate the total distance Laura drives to school and back every day
    school_distance = 20
    daily_distance = school_distance * 2

    # Calculate the total distance Laura drives to the supermarket twice a week
    supermarket_distance = school_distance + 10
    weekly_supermarket_distance = supermarket_distance * 2

    # Calculate the total weekly distance Laura drives
    total_weekly_distance = daily_distance + weekly_supermarket_distance
    result = total_weekly_distance
    return result

print(solution())