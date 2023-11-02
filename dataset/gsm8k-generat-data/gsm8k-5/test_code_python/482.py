def solution():
    laps_per_night = 5  # Ian does 5 laps around the complex every night
    distance_per_lap = 100  # Each lap is 100 feet
    total_distance_per_night = laps_per_night * distance_per_lap  # Calculate total distance Ian jogs per night

    distance_per_calorie = 25  # Ian burns 1 calorie per 25 feet of jogging
    calories_per_night = total_distance_per_night / distance_per_calorie  # Calculate the number of calories Ian burns per night

    days = 5  # Ian jogs like this for 5 days
    total_calories = calories_per_night * days  # Calculate the total number of calories Ian burns after 5 days

    result = total_calories
    return result

print(solution())