def solution():
    """Mike changes tires on different vehicles.  He changes all the tires on 12 motorcycles and all the tires on 10 cars.  How many tires did he change?"""
    # Define the number of tires on each type of vehicle
    MOTORCYCLE_TIRES = 2
    CAR_TIRES = 4

    # Define the number of motorcycles and cars
    motorcycles = 12
    cars = 10

    # Calculate the total number of tires
    total_tires = motorcycles * MOTORCYCLE_TIRES + cars * CAR_TIRES

    # Display the total number of tires
    result = total_tires
    return result

print(solution())