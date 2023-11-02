def solution():
    monday_cars = 50
    tuesday_cars = 50
    wednesday_cars = monday_cars * 2
    thursday_cars = monday_cars * 2
    remaining_cars = (450 - (monday_cars + tuesday_cars + wednesday_cars + thursday_cars)) / 2
    result = remaining_cars
    return result

print(solution())