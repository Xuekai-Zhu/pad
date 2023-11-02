def solution():
    total_vehicles = 60
    ratio_cars_trucks = 2
    num_trucks = total_vehicles / (ratio_cars_trucks + 1)
    result = num_trucks
    return result

print(solution())