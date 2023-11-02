def solution():
    
    starting_cars = 14
    bought_cars = 28
    birthday_cars = 12
    given_away_cars = 8 + 3
    total_cars = starting_cars + bought_cars + birthday_cars - given_away_cars
    result = total_cars
    return result

print(solution())