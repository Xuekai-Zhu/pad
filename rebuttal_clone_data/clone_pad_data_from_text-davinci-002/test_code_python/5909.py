def solution():
     cars = 2
     wheels_per_car = 4
     bikes = 2
     trash_cans = 1
     wheels_per_trash_can = 2
     tricycle = 1
     wheels_per_tricycle = 3
     roller_skates = 2
 
     wheels = (cars * wheels_per_car) + (bikes * wheels_per_bike) + (trash_cans * wheels_per_trash_can) + (tricycle * wheels_per_tricycle) + (roller_skates)
 
     result = wheels
     return result

print(solution())