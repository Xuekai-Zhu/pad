def solution():
    """Jane's goal is to exercise 1 hour a day, 5 days a week.  If she hits her goal weekly for 8 weeks, how many hours has Jane exercised?"""
    # Define Jane's exercise goal per week
    GOAL_PER_WEEK = 5 * 1  # 5 days a week, 1 hour per day

    # Define the number of weeks Jane exercises
    weeks_exercising = 8

    # Calculate the total number of hours Jane exercises
    total_hours = GOAL_PER_WEEK * weeks_exercising

    # Display the total number of hours Jane exercises
    result = total_hours
    return result

print(solution())