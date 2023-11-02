def solution():
    """Jason is counting the number of cars that drive by his window. He counted four times as many green cars as red cars, and 6 more red cars than purple cars. If he counted 312 cars total, how many of them were purple?"""
    total_cars = 312
    green_cars = 4 * red_cars
    red_cars = purple_cars + 6
    purple_cars = (total_cars - green_cars) / 10
    result = purple_cars
    return result

print(solution())