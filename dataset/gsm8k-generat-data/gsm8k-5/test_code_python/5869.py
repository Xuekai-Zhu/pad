def solution():
    initial_cars = 14  # Jaden had 14 toy cars
    bought_cars = 28  # Jaden bought 28 cars from the toy store
    birthday_cars = 12  # Jaden got 12 cars for his birthday
    given_away_cars = 8 + 3  # Jaden gave 8 cars to his sister and 3 to his friend Vinnie

    # Calculate the total number of cars Jaden has left
    remaining_cars = initial_cars + bought_cars + birthday_cars - given_away_cars
    result = remaining_cars
    return result

print(solution())