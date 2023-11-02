def solution():
    total_vehicles = 300
    ratio = 2
    number_of_cars = total_vehicles / ratio
    number_of_trucks = total_vehicles - number_of_cars
    result = number_of_trucks
    return result

print(solution())