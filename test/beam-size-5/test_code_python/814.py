def solution():
    
    robert_cars = 20
    joe_cars = robert_cars * 2
    sold_cars = robert_cars * 0.2
    given_cars = sold_cars * 2
    remaining_cars = joe_cars - sold_cars - given_cars
    result = remaining_cars
    return result

print(solution())