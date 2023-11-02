def solution():
     lollipop_cost = 1.50
     gummy_cost = 2.00
     lollipops_bought = 4
     gummies_bought = 2
     total_cost = (lollipop_cost * lollipops_bought) + (gummy_cost * gummies_bought)
     money_left = 15 - total_cost
     result = money_left
     return result

print(solution())