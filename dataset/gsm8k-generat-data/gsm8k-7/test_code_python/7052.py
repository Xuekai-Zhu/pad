def solution():
    # Calculate the distance Felix would cover at his normal speed for 4 hours
    normal_speed_distance = 66 * 4
    # Calculate Felix's faster speed
    faster_speed = 66 * 2
    # Calculate the distance Felix would cover at his faster speed for 4 hours
    faster_speed_distance = faster_speed * 4
    # Add the two distances together to get the total distance Felix would cover
    total_distance = normal_speed_distance + faster_speed_distance
    result = total_distance
    return result

print(solution())