def solution():
    """There are 516 cars in a parking lot. One-third are blue, one-half are red, and the rest are black. How many black cars are on the lot?"""
    # Calculate the number of blue cars
    blue_cars = 516/3

    # Calculate the number of red cars
    red_cars = 516/2

    # Calculate the number of black cars
    black_cars = 516 - blue_cars - red_cars

    # Display the number of black cars
    result = black_cars
    return result

print(solution())