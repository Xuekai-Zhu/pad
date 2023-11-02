def solution():
    # Calculate the total number of cars in all packages
    total_cars = 10 * 5

    # Calculate the number of cars given to each nephew
    cars_per_nephew = total_cars * (1/5)

    # Calculate the total number of cars given to both nephews
    total_given_cars = cars_per_nephew * 2

    # Calculate the number of cars left with Tom
    cars_left = total_cars - total_given_cars
    result = cars_left
    return result

print(solution())