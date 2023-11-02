def solution():
    """Jaden had 14 toy cars. Then he bought 28 cars from the toy store and got 12 cars for his birthday. Jaden gave 8 of the toy cars to his sister and 3 to his friend Vinnie. How many toy cars does Jaden have left?"""
    starting_cars = 14
    bought_cars = 28
    birthday_cars = 12
    given_away_cars = 8 + 3
    total_cars = starting_cars + bought_cars + birthday_cars - given_away_cars
    result = total_cars
    return result

print(solution())