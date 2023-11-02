def solution():
    """John is very unfit and decides to work up to doing a push-up. He trains 5 days a week for them and starts with wall push-ups. He adds 1 rep a day and once he gets to 15 reps he will start training high elevation push-ups. and then low elevation push-ups, and finally floor push-ups. How many weeks will it take him to get to floor push-ups?"""
    days_per_week = 5
    reps_per_day = 1
    starting_reps = 1
    target_reps = 15
    weeks_to_reach_high_elevation = (target_reps - starting_reps)/(days_per_week * reps_per_day)
    high_elevation_reps = 20
    low_elevation_reps = 30
    floor_reps = 50
    total_weeks = weeks_to_reach_high_elevation + ((high_elevation_reps - target_reps) / (days_per_week * reps_per_day)) + ((low_elevation_reps - high_elevation_reps) / (days_per_week * reps_per_day)) + ((floor_reps - low_elevation_reps) / (days_per_week * reps_per_day))
    result = total_weeks
    return result

print(solution())