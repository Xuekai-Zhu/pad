def solution():
    """Gretchen read that you should spend 10 minutes walking for every 90 minutes you spend sitting. If Gretchen spends 6 hours working at her desk, how long will she spend walking?"""
    # Define the time Gretchen spends working at her desk in minutes
    work_time = 6 * 60

    # Calculate the number of 90 minute intervals Gretchen spends sitting
    sitting_intervals = work_time // 90

    # Calculate the total walking time needed based on the sitting intervals
    walking_time = sitting_intervals * 10

    # return the result in hours and minutes
    result_hours = walking_time // 60
    result_minutes = walking_time % 60
    result = (result_hours, result_minutes)
    return result

print(solution())