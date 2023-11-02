def solution():
    distance_per_hour = 2  # Cheryl walks 2 miles every hour
    hours_walked = 3  # Cheryl walks for 3 hours before turning back

    # Calculate the distance Cheryl walked away from home
    distance_away = distance_per_hour * hours_walked

    # Calculate the total distance Cheryl walked
    total_distance = distance_away * 2  # Cheryl walks back home, covering the same distance

    result = total_distance
    return result

print(solution())