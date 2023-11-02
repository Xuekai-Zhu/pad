def solution():
    """Geli is committed to her 3 times a week workout. On her first day, she started doing 10 push-ups. Her fitness trainer encouraged her to add 5 more push-ups each day. How many push-ups will she do in total throughout her first week?"""
    # Define the initial number of push-ups and the number of days in a week
    STARTING_PUSHUPS = 10
    DAYS_IN_WEEK = 7

    # Define the number of push-ups Geli will do each day
    daily_pushups = [STARTING_PUSHUPS + 5*i for i in range(DAYS_IN_WEEK)]

    # Calculate the total number of push-ups Geli will do in the first week
    total_pushups = sum(daily_pushups)

    # Display the total number of push-ups
    result = total_pushups
    return result

print(solution())