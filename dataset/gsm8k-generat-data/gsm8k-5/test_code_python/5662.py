def solution():
    canoe_speed = 10  # Karen's speed on still water is 10 miles per hour
    river_speed = 4  # The river flows in the opposite direction at 4 miles per hour
    river_length = 12  # The river is 12 miles long

    # Calculate the net speed of Karen's canoe against the current
    net_speed = canoe_speed - river_speed

    # Calculate the time it will take Karen to paddle up the river
    time = river_length / net_speed
    result = time
    return result

print(solution())