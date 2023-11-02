def solution():
    """Erik's dog can run 24 miles per hour. It is chasing a rabbit that can run 15 miles per hour. The rabbit has a head start of .6 miles. How many minutes does it take for the dog to catch up to the rabbit?"""
    dog_speed = 24/60 # miles per minute
    rabbit_speed = 15/60 # miles per minute
    head_start = 0.6
    distance_to_cover = head_start
    time = 0
    while distance_to_cover > 0:
        distance_to_cover -= (dog_speed - rabbit_speed)
        time += 1
    result = time
    return result

print(solution())