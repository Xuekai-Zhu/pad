def solution():
    """Joanne makes $16.00 working at her main job for 8 hours a day.  She has a part-time job, working an extra 2 hours a day where she makes $13.50 an hour.  How much money does she make if she works this schedule 5 days a week?"""
    # Define Joanne's regular rate and part-time rate
    REGULAR_RATE = 16
    PART_TIME_RATE = 13.5

    # Define Joanne's regular hours and part-time hours
    REGULAR_HOURS = 8
    PART_TIME_HOURS = 2

    # Calculate Joanne's weekly earnings
    weekly_earnings = (REGULAR_RATE * REGULAR_HOURS + PART_TIME_RATE * PART_TIME_HOURS) * 5

    # Display Joanne's weekly earnings
    result = weekly_earnings
    return result

print(solution())