def solution():
     book_costs = [25.00, 18.00, 21.00, 35.00, 12.00, 10.00]
     discounts = [30, 20]
     total_cost = 0
     for cost in book_costs:
         if cost > 22.00:
             total_cost += cost - (cost * (discounts[0]/100))
         elif cost < 20.00:
             total_cost += cost - (cost * (discounts[1]/100))
         else:
             total_cost += cost
     result = total_cost
     return result

print(solution())