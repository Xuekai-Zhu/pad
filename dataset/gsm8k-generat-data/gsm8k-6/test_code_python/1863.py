def solution():
    # Calculate the distance between Edmonton and Calgary
    distance_EC = 220 + 110  # distance between Edmonton and Red Deer + distance between Red Deer and Calgary

    # Calculate the time it takes to travel from Edmonton to Calgary at 110 km/hour
    time = distance_EC / 110
    result = time
    return result

print(solution())