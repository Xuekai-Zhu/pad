def solution():
    """Mike changes tires on different vehicles. He changes all the tires on 12 motorcycles and all the tires on 10 cars. How many tires did he change?"""
    # Define the number of tires on a motorcycle and a car
    TIRE_PER_MOTORCYCLE = 2
    TIRE_PER_CAR = 4

    # Calculate the total number of tires on the motorcycles
    motorcycle_tires = 12 * TIRE_PER_MOTORCYCLE

    # Calculate the total number of tires on the cars
    car_tires = 10 * TIRE_PER_CAR

    # Calculate the total number of tires changed
    total_tires = motorcycle_tires + car_tires

    # return the result
    result = total_tires
    return result

print(solution())