def solution():
    starting_exercise = "wall push-ups"
    elevation_change = "high elevation push-ups"
    target_exercise = "floor push-ups"
    days_per_week = 5
    reps_per_day = 1
    goal_reps = 15
    weeks = 0
    while starting_exercise != target_exercise:
        if reps_per_day == goal_reps:
            if starting_exercise == "wall push-ups":
                starting_exercise = elevation_change
                reps_per_day = 1
                weeks += 1
            elif starting_exercise == "high elevation push-ups":
                starting_exercise = "low elevation push-ups"
                reps_per_day = 1
                weeks += 1
            elif starting_exercise == "low elevation push-ups":
                starting_exercise = target_exercise
                reps_per_day = 1
                weeks += 1
        else:
            reps_per_day += 1
    return weeks

print(solution())