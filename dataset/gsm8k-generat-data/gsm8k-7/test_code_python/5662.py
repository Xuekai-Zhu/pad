def solution():
    canoe_speed = 10
    river_speed = 4
    river_length = 12

    # Calculate the net speed of Karen's canoe against the current
    net_speed = canoe_speed - river_speed

    # Calculate the time it will take Karen to paddle up the river
    time = river_length / net_speed
    result = time
    return result

print(solution())