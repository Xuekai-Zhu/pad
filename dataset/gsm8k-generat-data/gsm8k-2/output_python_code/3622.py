def solution():
    """Mark is a lawyer who works at the county courthouse every day. It takes him 5 minutes to find parking and 3 minutes to walk into the courthouse. 2 days of the week it takes him 30 minutes to get through the metal detector and the other 3 days are less crowded so he gets through in 10 minutes. How long does he spend on all these activities in a week with 5 work days?"""
    parking_time = 5
    walking_time = 3
    crowded_days_metal_detector_time = 30
    less_crowded_days_metal_detector_time = 10
    total_work_days = 5

    metal_detector_time = crowded_days_metal_detector_time * 2 + less_crowded_days_metal_detector_time * 3
    total_time = (parking_time + walking_time + metal_detector_time) * total_work_days

    result = total_time
    return result

print(solution())