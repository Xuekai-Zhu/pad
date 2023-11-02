def solution():
    """Jonathan enjoys walking and running for exercise, and he has three different exercise routines.  On Mondays, he walks at 2 miles per hour.  On Wednesdays, he walks at 3 miles per hour.  And on Fridays, he runs at 6 miles per hour.  On each exercise day, he travels 6 miles.  What is the combined total time, in hours, he spends exercising in a week?"""
    # Define the distance traveled on each exercise day
    DISTANCE = 6

    # Calculate the time spent exercising on Monday
    time_monday = DISTANCE / 2

    # Calculate the time spent exercising on Wednesday
    time_wednesday = DISTANCE / 3

    # Calculate the time spent exercising on Friday
    time_friday = DISTANCE / 6

    # Calculate the total time spent exercising in a week
    total_time = time_monday + time_wednesday + time_friday

    # Display the total time spent exercising in a week
    result = total_time
    return result

print(solution())