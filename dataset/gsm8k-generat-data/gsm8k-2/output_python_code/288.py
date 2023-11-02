def solution():
    """Jim collects model cars, and he has 301 models total. Jim has 4 times as many Buicks as Fords,
    and 3 more than twice the number of Fords than Chevys. How many Buicks does Jim have?"""
    total_cars = 301
    chevy_cars = (total_cars - 3) / 7
    ford_cars = 2 * chevy_cars + 3
    buick_cars = 4 * ford_cars
    result = buick_cars
    return result

print(solution())