def solution():
    """John and Jack have 30 minutes to walk to school together. It takes them 6 minutes to get to the corner where the library is. It takes them another 13 minutes to get to the fire station. How much longer do they have to get to school without being late?"""
    total_time = 30
    time_to_library = 6
    time_to_fire_station = 13
    time_left = total_time - time_to_library - time_to_fire_station
    result = time_left
    return result

print(solution())