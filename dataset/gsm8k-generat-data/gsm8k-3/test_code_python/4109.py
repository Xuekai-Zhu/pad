def solution():
    """Kristine traveled to Paris in France to visit her friend. On the way, she has driven a train for 300 km and a bus for half that distance. After arriving in the city, she had to take a cab and drove three times fewer kilometers than she rode the bus. How many kilometers in total had Kristine traveled to reach her destination?"""
    # Define the distance Kristine traveled by train
    train_distance = 300

    # Define the distance Kristine traveled by bus
    bus_distance = train_distance / 2

    # Define the distance Kristine traveled by cab
    cab_distance = bus_distance / 3

    # Calculate the total distance Kristine traveled
    total_distance = train_distance + bus_distance + cab_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())