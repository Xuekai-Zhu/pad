def solution():
    original_cars = 200
    door_per_car = 5
    decreased_cars = 50
    decreased_cars_2 = 50
    total_cars = original_cars - decreased_cars - decreased_cars_2
    total_doors = total_cars * door_per_car
    result = total_doors
    return result

print(solution())