def solution():
    starting_pushups = 0
    max_pushups_per_set = 15
    training_days_per_week = 5

    # Calculate the number of weeks it will take John to get to high elevation pushups
    high_elevation_pushups = max_pushups_per_set * 4  # 4 weeks of increasing reps
    weeks_to_high_elevation = int(
        ((high_elevation_pushups - starting_pushups) / max_pushups_per_set) / (training_days_per_week / 7))

    # Calculate the number of weeks it will take John to get to low elevation pushups
    low_elevation_pushups = max_pushups_per_set * 3  # 3 weeks of increasing reps
    weeks_to_low_elevation = int(((low_elevation_pushups - high_elevation_pushups) / max_pushups_per_set) / (
            training_days_per_week / 7)) + weeks_to_high_elevation

    # Calculate the number of weeks it will take John to get to floor pushups
    floor_pushups = max_pushups_per_set * 2  # 2 weeks of increasing reps
    weeks_to_floor_pushups = int(
        ((floor_pushups - low_elevation_pushups) / max_pushups_per_set) / (training_days_per_week / 7)) + weeks_to_low_elevation

    result = weeks_to_floor_pushups
    return result

print(solution())