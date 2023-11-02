def solution():
    
    total_cars = 125
    regular_cars_percent = 0.64
    truck_percent = 0.08
    regular_cars = total_cars * regular_cars_percent
    trucks = total_cars * truck_percent
    convertibles = total_cars - regular_cars - trucks
    result = convertibles
    return result

print(solution())