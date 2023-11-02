def solution():
    
    total_cars = 450
    monday_cars = 50
    tuesday_cars = 50
    wednesday_cars = 2 * monday_cars
    thursday_cars = 2 * monday_cars
    remaining_days_cars = (total_cars - monday_cars - tuesday_cars - wednesday_cars - thursday_cars) / 3
    result = remaining_days_cars
    return result

print(solution())