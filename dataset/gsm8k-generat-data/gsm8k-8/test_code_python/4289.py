def solution():
    # Define the total distance and distance at race pace
    total_distance = 10
    race_pace_distance = 4

    # Calculate the distance ridden slowly
    slow_distance = (total_distance - race_pace_distance) / 2

    # Calculate the distance from Layla's house to the high school
    distance_to_high_school = slow_distance + race_pace_distance
    result = distance_to_high_school
    return result

print(solution())