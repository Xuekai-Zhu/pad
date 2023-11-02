def solution():
    """Jim collects model cars, and he has 301 models total.  Jim has 4 times as many Buicks as Fords, and 3 more than twice the number of Fords than Chevys.  How many Buicks does Jim have?"""
    # Define the total number of cars
    total_cars = 301

    # Calculate the number of Chevys
    chevy_cars = (total_cars - 3) / 7

    # Calculate the number of Fords
    ford_cars = 2 * chevy_cars

    # Calculate the number of Buicks
    buick_cars = 4 * ford_cars

    # Return the number of Buicks
    result = buick_cars
    return result

print(solution())