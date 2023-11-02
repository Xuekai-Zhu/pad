def solution():
    unloaded_speed = 20  # miles per hour
    loaded_speed = 10  # miles per hour
    unloaded_distance = 260  # sum of distances for the unloaded sled
    loaded_distance = 260  # sum of distances for the loaded sled
    total_time = (180/loaded_speed) + (120/unloaded_speed) + (80/loaded_speed) + (140/unloaded_speed)  # time in hours
    result = total_time
    return result

print(solution())