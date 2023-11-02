def solution():
    """Jason has to drive home which is 120 miles away. If he drives at 60 miles per hour for 30 minutes, what speed does he have to average for the remainder of the drive to get there in exactly 1 hour 30 minutes?"""
    total_distance = 120
    first_half_distance = 60
    first_half_time = 0.5  # 30 minutes in hours
    second_half_distance = total_distance - first_half_distance
    second_half_time = 1.5 - first_half_time  # remaining time left to reach (1 hour 30 minutes - 30 minutes)
    
    # speed = distance / time
    # to get the average speed, we need the total time and total distance.
    total_time = first_half_time + second_half_time
    average_speed = total_distance / total_time
    
    # to calculate the speed needed for the remaining half, we use the formula
    # speed = distance / time
    # solving for time, we get
    time_needed = second_half_distance / (average_speed - 60)
    
    # to get the speed for the remaining half of the drive, we use the distance and time calculated above
    remaining_speed = second_half_distance / time_needed
    
    result = remaining_speed
    return result

print(solution())