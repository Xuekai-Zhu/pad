def solution():
    """Tom bought 10 packages of miniature racing cars. Each package contains five cars. He gave each of his two nephews 1/5 of the cars. How many miniature racing cars are left with Tom?"""
    # Define the initial number of cars
    initial_cars = 10 * 5

    # Calculate the number of cars given to each nephew
    nephew_cars = (1/5) * initial_cars

    # Calculate the number of cars left with Tom
    cars_left = initial_cars - (2 * nephew_cars)

    result = cars_left
    return result

print(solution())