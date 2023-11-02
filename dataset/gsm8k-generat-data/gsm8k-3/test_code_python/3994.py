def solution():
    """Tom bought 10 packages of miniature racing cars. Each package contains five cars. He gave each of his two nephews 1/5 of the cars. How many miniature racing cars are left with Tom?"""
    # Define the number of packages and cars per package
    PACKAGES = 10
    CARS_PER_PACKAGE = 5

    # Calculate the total number of cars Tom bought
    total_cars = PACKAGES * CARS_PER_PACKAGE

    # Calculate the number of cars Tom gave to each nephew
    cars_per_nephew = total_cars * 1/5

    # Calculate the number of cars left with Tom
    cars_left = total_cars - (2 * cars_per_nephew)

    # Display the number of cars left with Tom
    result = cars_left
    return result

print(solution())