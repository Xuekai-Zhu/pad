def solution():
    cars = 15
    bicycles = 3
    trucks = 8
    tricycle = 1
    tires_on_cars = cars * 4
    tires_on_bicycles = bicycles * 2
    tires_on_trucks = trucks * 6
    tires_on_tricycle = tricycle * 3
    total_tires = tires_on_cars + tires_on_bicycles + tires_on_trucks + tires_on_tricycle
    result = total_tires
    
    return result

print(solution())