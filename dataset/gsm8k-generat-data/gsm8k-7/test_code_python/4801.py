def solution():
    days_per_week = 5
    hours_per_day = 1.5
    speed = 8  # in miles per hour

    # Calculate the distance run per day
    distance_per_day = speed * hours_per_day

    # Calculate the total distance run per week
    total_distance = distance_per_day * days_per_week

    result = total_distance
    return result

print(solution())