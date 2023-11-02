def solution():
     total_cars = 71
     engine = 1
     caboose = 1
     cargo_cars = ((total_cars - engine - caboose)/2) - 3
     passenger_cars = total_cars - engine - caboose - cargo_cars
     result = passenger_cars
     return result

print(solution())