def solution():
    
    tuesday_cars = 25
    monday_cars = 0.8 * tuesday_cars
    wednesday_cars = monday_cars + 2
    thursday_cars = 10
    friday_cars = 10
    weekend_cars = 5 * 2
    total_cars = tuesday_cars + monday_cars + wednesday_cars + thursday_cars + friday_cars + weekend_cars
    result = total_cars
    return result

print(solution())