def solution():
    # Calculate the speeds on different terrains
    flat_speed = 60
    downhill_speed = flat_speed + 12
    uphill_speed = flat_speed - 18

    # Calculate the average speed
    avg_speed = (1/3)*flat_speed + (1/3)*downhill_speed + (1/3)*uphill_speed
    result = avg_speed
    return result

print(solution())