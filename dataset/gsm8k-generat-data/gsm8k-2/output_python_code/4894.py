def solution():
    """Christina and her friend are driving across the state. When Christina is driving the speed limit is 30 miles per hour. When her friend is driving, the speed limit is 40 miles per hour. The drive is 210 miles total. If her friend drives for 3 hours and both drive at the speed limit, how many minutes will Christina drive?"""
    total_distance = 210
    christina_speed = 30
    friend_speed = 40
    friend_time = 3
    friend_distance = friend_speed * friend_time
    christina_distance = total_distance - friend_distance
    christina_time = christina_distance / christina_speed
    christina_time_in_minutes = christina_time * 60
    result = christina_time_in_minutes
    return result

print(solution())