def solution():
    laps_per_night = 5
    distance_per_lap = 100
    calories_burned_per_distance = 1/25

    num_days = 5
    total_laps = laps_per_night * num_days

    # Calculate the total distance Ian jogs
    total_distance = total_laps * distance_per_lap

    # Calculate the total calories Ian burns
    total_calories_burned = total_distance * calories_burned_per_distance
    result = total_calories_burned
    return result

print(solution())