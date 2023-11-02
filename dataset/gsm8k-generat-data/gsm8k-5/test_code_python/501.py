def solution():
    starting_reps = 0  # John starts with no push-ups
    max_reps = 15  # John can do 15 reps of wall push-ups before moving to high elevation push-ups
    pushup_sets_per_day = 1  # John adds 1 rep per day
    days_per_week = 5  # John trains 5 days a week

    # Calculate the number of weeks it will take John to reach floor push-ups
    weeks_to_high_elevation = (max_reps - starting_reps) / (pushup_sets_per_day * days_per_week)
    weeks_to_low_elevation = weeks_to_high_elevation + (max_reps / (pushup_sets_per_day * days_per_week))
    weeks_to_floor_pushups = weeks_to_low_elevation + (max_reps / (pushup_sets_per_day * days_per_week))

    result = weeks_to_floor_pushups
    return result

print(solution())