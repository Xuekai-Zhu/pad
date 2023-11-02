def solution():
    """Geli is committed to her 3 times a week workout. On her first day, she started doing 10 push-ups. Her fitness trainer encouraged her to add 5 more push-ups each day. How many push-ups will she do in total throughout her first week?"""
    days_per_week = 7
    workout_days = 3
    starting_pushups = 10
    pushup_increase = 5
    total_pushups = 0
    
    for i in range(workout_days):
        pushups = starting_pushups + (pushup_increase * i)
        total_pushups += pushups
    
    result = total_pushups * days_per_week
    return result

print(solution())