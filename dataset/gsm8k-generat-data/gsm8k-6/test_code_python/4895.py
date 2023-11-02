def solution():
    # Calculate the total driving time and distance
    total_distance = 210  # miles
    friend_time = 3  # hours
    friend_distance = 40 * friend_time  # miles
    christina_distance = total_distance - friend_distance  # miles
    christina_time = christina_distance / 30  # hours
    christina_minutes = christina_time * 60  # minutes
    result = christina_minutes
    return result

print(solution())