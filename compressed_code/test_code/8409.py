def solution():
    
    cars_planned = 200
    cars_shortage = 50
    final_cars = (cars_planned - cars_shortage) * 0.5
    doors_per_car = 5
    total_doors = final_cars * doors_per_car
    result = total_doors
    return result

print(solution())