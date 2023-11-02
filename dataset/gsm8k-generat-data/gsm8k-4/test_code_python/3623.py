def solution():
    """Mark is a lawyer who works at the county courthouse every day. It takes him 5 minutes to find parking and 3 minutes to walk into the courthouse. 2 days of the week it takes him 30 minutes to get through the metal detector and the other 3 days are less crowded so he gets through in 10 minutes. How long does he spend on all these activities in a week with 5 work days?"""
    # Define the time it takes to find parking and walk into the courthouse
    walk_time = 3
    parking_time = 5

    # Define the time it takes to get through the metal detector on crowded and less crowded days
    crowded_detector_time = 30
    less_crowded_detector_time = 10

    # Calculate the total time Mark spends on parking and walking every day
    total_time = walk_time + parking_time

    # Calculate the total time Mark spends on the metal detector each week
    total_detector_time = (2 * crowded_detector_time) + (3 * less_crowded_detector_time)

    # Calculate the total time Mark spends on all these activities in a week
    total_time_week = (total_time * 5) + total_detector_time

    # return the result
    result = total_time_week
    return result

print(solution())