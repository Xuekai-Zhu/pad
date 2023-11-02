def solution():
    """Geli is committed to her 3 times a week workout. On her first day, she started doing 10 push-ups. Her fitness trainer encouraged her to add 5 more push-ups each day. How many push-ups will she do in total throughout her first week?"""
    num_days = 7
    num_workouts = 3
    starting_pushups = 10
    pushup_increase = 5
    total_pushups = 0
    for i in range(num_days):
        if i % 7 < num_workouts:
            num_pushups = starting_pushups + (i // num_workouts) * pushup_increase
            total_pushups += num_pushups
    result = total_pushups
    return result

print(solution())