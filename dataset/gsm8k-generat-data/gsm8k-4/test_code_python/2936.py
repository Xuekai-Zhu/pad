def solution():
    """There are 516 cars in a parking lot. One-third are blue, one-half are red, and the rest are black. How many black cars are on the lot?"""
    # Define the total number of cars
    total_cars = 516

    # Calculate the number of blue cars
    blue_cars = total_cars * (1/3)

    # Calculate the number of red cars
    red_cars = total_cars * (1/2)

    # Calculate the number of black cars
    black_cars = total_cars - blue_cars - red_cars

    # return the result
    result = black_cars
    return result

print(solution())