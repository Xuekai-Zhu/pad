def solution():
     bracelet_cost = 15
     necklace_cost = 10
     mug_cost = 20
     total_cost = bracelet_cost * 3 + necklace_cost * 2 + mug_cost
     money_given = 100
     change = money_given - total_cost
     result = change
     return result

print(solution())