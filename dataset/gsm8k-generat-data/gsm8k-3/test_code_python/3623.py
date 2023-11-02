def solution():
    """Mark is a lawyer who works at the county courthouse every day. It takes him 5 minutes to find parking and 3 minutes to walk into the courthouse. 2 days of the week it takes him 30 minutes to get through the metal detector and the other 3 days are less crowded so he gets through in 10 minutes. How long does he spend on all these activities in a week with 5 work days?"""
    # Define the time it takes for each activity in minutes
    PARKING_TIME = 5
    WALKING_TIME = 3
    METAL_DETECTOR_CROWDED_TIME = 30
    METAL_DETECTOR_LESS_CROWDED_TIME = 10
    WORK_DAYS = 5

    # Calculate Mark's total time spent on activities in a week
    total_time = (PARKING_TIME + WALKING_TIME) * WORK_DAYS
    total_time += (METAL_DETECTOR_CROWDED_TIME * 2 + METAL_DETECTOR_LESS_CROWDED_TIME * 3)
    
    # Display the total time spent on activities
    result = total_time
    return result

print(solution())