def solution():
    """Bobby has 16 toy cars, and the number of cars he has increases by 50% every year. How many toy cars will Bobby have in three years?"""
    initial_cars = 16
    growth_rate = 1.5
    final_cars = initial_cars * (growth_rate ** 3)
    result = final_cars
    return result

print(solution())