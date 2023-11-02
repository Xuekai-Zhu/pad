def solution():
    """Yolanda leaves home for work at 7:00 AM, riding her bike at 20 miles per hour. 15 minutes after she leaves, her husband realizes that she forgot her lunch, and jumps in the car to bring it to her. If he drives at 40 miles per hour and follows the exact same route as Yolanda, how many minutes will it take him to catch her?"""
    yolanda_speed = 20 / 60  # converts mph to mpm
    husband_speed = 40 / 60  # converts mph to mpm
    time_since_yolanda_left = 15  # minutes
    distance_yolanda_covered = yolanda_speed * time_since_yolanda_left
    distance_remaining = 1  # fully catch up to yolanda
    time_to_catch_up = (distance_remaining - distance_yolanda_covered) / (husband_speed - yolanda_speed)
    total_time = time_since_yolanda_left + time_to_catch_up
    result = total_time
    return result

print(solution())