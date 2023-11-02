def solution():
    """Tommy goes for a run around his neighborhood and decides to calculate how many wheels he saw. All the trucks in his neighborhood have 4 wheels and all the cars in his neighborhood also have 4 wheels. If he saw 12 trucks and 13 cars, how many wheels did he see?"""
    # Calculate the total number of wheels on the trucks
    truck_wheels = 12 * 4

    # Calculate the total number of wheels on the cars
    car_wheels = 13 * 4

    # Calculate the total number of wheels seen by Tommy
    total_wheels = truck_wheels + car_wheels

    # Display the total number of wheels seen by Tommy
    result = total_wheels
    return result

print(solution())