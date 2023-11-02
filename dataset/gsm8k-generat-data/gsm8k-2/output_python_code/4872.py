def solution():
    """Erik's dog can run 24 miles per hour. It is chasing a rabbit that can run 15 miles per hour. The rabbit has a head start of .6 miles. How many minutes does it take for the dog to catch up to the rabbit?"""
    dog_speed = 24
    rabbit_speed = 15
    head_start = 0.6
    distance_difference = dog_speed - rabbit_speed
    time_to_catch_up = head_start / distance_difference * 60
    result = time_to_catch_up
    return result

print(solution())