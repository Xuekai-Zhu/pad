def solution():
    """John is very unfit and decides to work up to doing a push-up. He trains 5 days a week for them and starts with wall push-ups. He adds 1 rep a day and once he gets to 15 reps he will start training high elevation push-ups. and then low elevation push-ups, and finally floor push-ups. How many weeks will it take him to get to floor push-ups?"""
    reps_per_day = 1
    days_per_week = 5
    starting_reps = 0
    high_elevation_reps = 15
    low_elevation_reps = 25
    training_weeks = 0
    while starting_reps < low_elevation_reps:
        for i in range(days_per_week):
            starting_reps += reps_per_day
        if starting_reps >= low_elevation_reps:
            break
        elif starting_reps >= high_elevation_reps:
            reps_per_day = 2
        else:
            reps_per_day = 1
        training_weeks += 1
    result = training_weeks
    return result

print(solution())