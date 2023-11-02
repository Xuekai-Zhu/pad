def solution():
     oil_change_cost = 20
     repair_cost = 30
     car_wash_cost = 5
     cars_oiled = 5
     cars_repaired = 10
     cars_washed = 15
     total_cost = (oil_change_cost * cars_oiled) + (repair_cost * cars_repaired) + (car_wash_cost * cars_washed)
     result = total_cost
     return result

print(solution())