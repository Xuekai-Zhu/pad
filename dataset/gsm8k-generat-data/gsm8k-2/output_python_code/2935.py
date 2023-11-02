def solution():
    """There are 516 cars in a parking lot. One-third are blue, one-half are red, and the rest are black. How many black cars are on the lot?"""
    total_cars = 516
    blue_cars = total_cars // 3
    red_cars = total_cars // 2
    black_cars = total_cars - blue_cars - red_cars
    result = black_cars
    return result

print(solution())