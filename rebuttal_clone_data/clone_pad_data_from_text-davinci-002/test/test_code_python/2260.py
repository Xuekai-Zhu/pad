def solution():
    total_cars = 10 * 5
    cars_given_away = 2 * (1/5 * total_cars)
    cars_left = total_cars - cars_given_away
    result = cars_left
    
    return result

print(solution())