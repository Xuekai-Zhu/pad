def solution():
    # Calculate the distance Kristine traveled by bus
    bus_distance = 300 / 2

    # Calculate the distance Kristine traveled by cab
    cab_distance = bus_distance / 3

    # Calculate the total distance Kristine traveled
    total_distance = bus_distance + cab_distance + 300

    result = total_distance
    return result

print(solution())