def solution():
     cars = 19
     wheels_per_car = 5
     total_wheels = 117
     motorcycle_wheels = total_wheels - (cars * wheels_per_car)
     motorcycles = motorcycle_wheels / 2
     result = motorcycles
     return result

print(solution())