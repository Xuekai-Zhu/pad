def solution():
    """Jason is counting the number of cars that drive by his window. He counted four times as many green cars as red cars, and 6 more red cars than purple cars. If he counted 312 cars total, how many of them were purple?"""
    total_cars = 312
    purple_cars = total_cars / 15
    red_cars = purple_cars + 6
    green_cars = red_cars * 4
    result = purple_cars
    return result

print(solution())