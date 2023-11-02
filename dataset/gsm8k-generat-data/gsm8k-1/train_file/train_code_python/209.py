def solution():
    """Bobby has 16 toy cars, and the number of cars he has increases by 50% every year. How many toy cars will Bobby have in three years?"""
    initial_cars = 16
    growth_factor = 1.5
    total_cars = initial_cars * (growth_factor ** 3)
    result = total_cars
    return result

print(solution())