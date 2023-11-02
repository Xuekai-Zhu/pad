def solution():
    """Jason is counting the number of cars that drive by his window. He counted four times as many green cars as red cars, and 6 more red cars than purple cars. If he counted 312 cars total, how many of them were purple?"""

    # Let x be the number of purple cars
    purple_cars = x

    # Red cars are 6 more than purple cars
    red_cars = x + 6

    # Green cars are 4 times the number of red cars
    green_cars = 4 * red_cars

    # Total number of cars is the sum of all three colors
    total_cars = purple_cars + red_cars + green_cars

    # Set up the equation to solve for x
    total_cars = 312
    x = (312 - 4 * (x + 6)) / 10

    # Final answer is the number of purple cars
    result = x
    return result

print(solution())