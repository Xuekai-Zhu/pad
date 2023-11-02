def solution():
     stocking_cost = 20
     stocking_discount = 10
     stocking_monogram_cost = 5
     total_stockings = 5 + 4
     total_cost = (total_stockings * stocking_cost) - ((total_stockings * stocking_cost) * (stocking_discount / 100)) + (total_stockings * stocking_monogram_cost)
     result = total_cost
     return result

print(solution())