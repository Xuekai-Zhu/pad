def solution():
    """Jane's goal is to exercise 1 hour a day, 5 days a week. If she hits her goal weekly for 8 weeks, how many hours has Jane exercised?"""
    # Define the number of days in a week and the number of weeks
    DAYS_IN_WEEK = 5
    WEEKS = 8

    # Define the goal number of hours Jane wants to exercise
    GOAL_HOURS = 1

    # Calculate the total number of hours Jane exercises in the 8-week period
    total_hours = GOAL_HOURS * DAYS_IN_WEEK * WEEKS

    # return the result
    result = total_hours
    return result

print(solution())