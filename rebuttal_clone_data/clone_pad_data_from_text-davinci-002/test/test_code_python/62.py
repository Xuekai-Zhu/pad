def solution():
    
    cars_on_tuesday = 25
    cars_on_monday = cars_on_tuesday * 0.8
    cars_on_wednesday = cars_on_monday + 2
    cars_on_thursday = 10
    cars_on_friday = 10
    cars_on_saturday = 5
    cars_on_sunday = 5
    total_cars = cars_on_tuesday + cars_on_monday + cars_on_wednesday + cars_on_thursday + cars_on_friday + cars_on_saturday + cars_on_sunday
    result = total_cars
    return result

print(solution())