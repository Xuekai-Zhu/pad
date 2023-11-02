def solution():
     money = 17.80
     car_cost = 0.95
     track_cost = 6.00
     cars_bought = 4
     car_total = car_cost * cars_bought
     money_left = money - car_total - track_cost
     result = money_left
 
     return result

print(solution())