def solution():
     """Mary bought 5 boxes of drinks at $6 each box and 10 boxes of pizzas at $14 each box for her pizza party. She paid $200 for all the items. How much change did she get back?"""
     drink_cost = 6
     pizza_cost = 14
     total_cost = drink_cost * 5 + pizza_cost * 10
     paid_amount = 200
     change = paid_amount - total_cost
     result = change
     return result

print(solution())