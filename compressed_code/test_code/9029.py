def solution():
    
    train_distance = 300
    bus_distance = train_distance / 2
    cab_distance = bus_distance / 3
    total_distance = train_distance + bus_distance + cab_distance
    result = total_distance
    return result

print(solution())