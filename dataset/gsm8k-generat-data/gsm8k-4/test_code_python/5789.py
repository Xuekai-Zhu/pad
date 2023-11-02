def solution():
    """Jonathan enjoys walking and running for exercise, and he has three different exercise routines. On Mondays, he walks at 2 miles per hour. On Wednesdays, he walks at 3 miles per hour. And on Fridays, he runs at 6 miles per hour. On each exercise day, he travels 6 miles. What is the combined total time, in hours, he spends exercising in a week?"""
    # Define the distances and speeds for each exercise routine
    distance_monday = 6
    speed_monday = 2

    distance_wednesday = 6
    speed_wednesday = 3

    distance_friday = 6
    speed_friday = 6

    # Calculate the total time spent exercising
    time_monday = distance_monday / speed_monday
    time_wednesday = distance_wednesday / speed_wednesday
    time_friday = distance_friday / speed_friday

    total_time = time_monday + time_wednesday + time_friday

    # return the result
    result = total_time
    return result

print(solution())