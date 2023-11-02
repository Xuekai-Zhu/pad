def solution():
    """Jason has to drive home which is 120 miles away. If he drives at 60 miles per hour for 30 minutes, what speed does he have to average for the remainder of the drive to get there in exactly 1 hour 30 minutes?"""
    total_distance = 120
    initial_speed = 60
    initial_time = 0.5  # 30 minutes = 0.5 hours
    remaining_distance = total_distance - (initial_speed * initial_time)
    remaining_time = 1.5 - initial_time
    remaining_speed = remaining_distance / remaining_time
    result = remaining_speed
    return result

print(solution())