def solution():
    # Define the number of reps per set for each type of push-up
    wall_reps = 15
    high_elevation_reps = 20
    low_elevation_reps = 25
    floor_reps = 30

    # Define the number of reps added per day
    reps_added_per_day = 1

    # Starting from wall push-ups, calculate the number of days to reach each type of push-up
    days_to_high_elevation = (wall_reps - 1) // reps_added_per_day
    days_to_low_elevation = (high_elevation_reps - wall_reps) // reps_added_per_day
    days_to_floor = (floor_reps - high_elevation_reps) // reps_added_per_day

    # Calculate the total number of weeks
    total_days = days_to_high_elevation + days_to_low_elevation + days_to_floor
    total_weeks = total_days // 7

    result = total_weeks
    return result

print(solution())