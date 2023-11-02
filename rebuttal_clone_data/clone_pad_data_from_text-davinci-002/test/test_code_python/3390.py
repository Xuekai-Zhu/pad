def solution():
    cars_owned = 3500
    cars_given_away = 50
    desired_cars = 500
    years_until_goal = (cars_owned - desired_cars) / cars_given_away
    result = years_until_goal
    
    return result

print(solution())