def solution():
    # Calculate the distance traveled by bus
    bus_distance = 300 / 2

    # Calculate the distance traveled by cab
    cab_distance = bus_distance / 3

    # Calculate the total distance traveled
    total_distance = 300 + bus_distance + cab_distance

    result = total_distance
    return result

print(solution())