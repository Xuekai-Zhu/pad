def solution():
     apple_cost = 1.25
     bike_cost = 80
     repair_cost = bike_cost * 0.25
     final_cost = repair_cost + bike_cost
     final_profit = final_cost * 0.20
     number_of_apples = final_profit / apple_cost
     result = number_of_apples
     
     return result

print(solution())