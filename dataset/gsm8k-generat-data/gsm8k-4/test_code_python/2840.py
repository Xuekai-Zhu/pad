def solution():
    """In a parking lot, there are cars and motorcycles. Each car has 5 wheels (including one spare) and each motorcycle has 2 wheels. There are 19 cars in the parking lot. Altogether all vehicles have 117 wheels. How many motorcycles are at the parking lot?"""
    # Define the number of wheels per car and per motorcycle
    car_wheels = 5
    motorcycle_wheels = 2

    # Define the number of cars and the total number of vehicles
    num_cars = 19
    total_vehicles = num_cars + num_motorcycles

    # Define the total number of wheels
    total_wheels = 117

    # Calculate the number of motorcycles
    num_motorcycles = (total_wheels - num_cars * car_wheels) // motorcycle_wheels

    # Return the result
    result = num_motorcycles
    return result

print(solution())