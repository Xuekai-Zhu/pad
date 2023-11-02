def solution():
    """Geli is committed to her 3 times a week workout. On her first day, she started doing 10 push-ups. Her fitness trainer encouraged her to add 5 more push-ups each day. How many push-ups will she do in total throughout her first week?"""
    # Define the number of push-ups on the first day and the increment per day
    first_day_pushups = 10
    increment_per_day = 5

    # Calculate the total number of push-ups in the first week
    pushups_per_week = 3 * (first_day_pushups + (first_day_pushups + increment_per_day) + (first_day_pushups + (2*increment_per_day)) + (first_day_pushups + (3*increment_per_day)) + (first_day_pushups + (4*increment_per_day)) + (first_day_pushups + (5*increment_per_day)) + (first_day_pushups + (6*increment_per_day)))

    # Return the result
    result = pushups_per_week
    return result

print(solution())