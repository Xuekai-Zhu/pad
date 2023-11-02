def solution():
     total_vehicles = 24
     motorcycles = total_vehicles / 3
     cars = total_vehicles - motorcycles
     cars_with_spare_tires = cars / 4
     total_tires = (cars - cars_with_spare_tires) + (motorcycles * 2)
     result = total_tires
     return result

print(solution())