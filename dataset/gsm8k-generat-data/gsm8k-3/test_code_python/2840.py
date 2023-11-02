def solution():
    """In a parking lot, there are cars and motorcycles.  Each car has 5 wheels (including one spare) and each motorcycle has 2 wheels. There are 19 cars in the parking lot. Altogether all vehicles have 117 wheels. How many motorcycles are at the parking lot?"""
    # Define the number of car wheels and motorcycle wheels
    CAR_WHEELS = 5
    MOTORCYCLE_WHEELS = 2

    # Define the number of cars in the parking lot
    cars = 19

    # Define the total number of wheels in the parking lot
    total_wheels = 117

    # Calculate the total number of car wheels in the parking lot
    car_wheels = cars * CAR_WHEELS

    # Calculate the total number of motorcycle wheels in the parking lot
    motorcycle_wheels = total_wheels - car_wheels

    # Calculate the number of motorcycles in the parking lot
    motorcycles = motorcycle_wheels // MOTORCYCLE_WHEELS

    # Display the number of motorcycles in the parking lot
    result = motorcycles
    return result

print(solution())