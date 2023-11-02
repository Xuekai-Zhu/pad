def solution():
    """If we assume all thirty 4-wheel drive cars in the parking lot have their spare tire with them, how many tires are in the parking lot?"""
    # Define the number of wheels per car and the number of cars
    WHEELS_PER_CAR = 4
    NUM_CARS = 30

    # Calculate the total number of wheels in the parking lot
    total_wheels = WHEELS_PER_CAR * NUM_CARS

    # Add in the number of spare tires
    total_tires = total_wheels + NUM_CARS

    # Display the total number of tires
    result = total_tires
    return result

print(solution())