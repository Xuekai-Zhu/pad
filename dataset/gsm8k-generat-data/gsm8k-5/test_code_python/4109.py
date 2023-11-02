def solution():
    train_distance = 300  # Kristine drove a train for 300 km
    bus_distance = train_distance / 2  # Kristine drove a bus for half the distance of the train
    cab_distance = bus_distance / 3  # Kristine drove a cab for three times less distance than she rode the bus

    # Calculate the total distance Kristine traveled
    total_distance = train_distance + bus_distance + cab_distance
    result = total_distance
    return result

print(solution())