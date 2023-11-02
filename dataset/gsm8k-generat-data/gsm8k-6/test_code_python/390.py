def solution():
    # Calculate the total distance Oscar will run before the marathon
    total_distance = 20 - 2  # Oscar has already run 2 miles
    added_distance_per_week = 2/3
    weeks_needed = total_distance / added_distance_per_week
    result = weeks_needed
    return result

print(solution())