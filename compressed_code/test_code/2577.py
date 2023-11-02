def solution():
    
    car_doors = 5
    planned_cars = 200
    metal_shortage_cars = planned_cars - 50
    pandemic_cars = metal_shortage_cars * 0.5
    total_cars = metal_shortage_cars - pandemic_cars
    total_doors = total_cars * car_doors
    result = total_doors
    return result

print(solution())