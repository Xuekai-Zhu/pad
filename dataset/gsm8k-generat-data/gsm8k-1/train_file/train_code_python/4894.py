def solution():
    """Christina and her friend are driving across the state. When Christina is driving the speed limit is 30 miles per hour. When her friend is driving, the speed limit is 40 miles per hour. The drive is 210 miles total. If her friend drives for 3 hours and both drive at the speed limit, how many minutes will Christina drive?"""
    
    # Calculate how many miles Christina will drive
    total_distance = 210
    friend_distance = 40 * 3
    christina_distance = total_distance - friend_distance
    
    # Calculate how long Christina will drive in minutes
    christina_speed = 30
    christina_time = christina_distance / christina_speed
    minutes_driving = christina_time * 60
    
    result = minutes_driving
    return result

print(solution())