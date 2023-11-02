def solution():
     
     drink_cost = 6
     pizza_cost = 14
     total_cost = drink_cost * 5 + pizza_cost * 10
     paid_amount = 200
     change = paid_amount - total_cost
     result = change
     return result

print(solution())