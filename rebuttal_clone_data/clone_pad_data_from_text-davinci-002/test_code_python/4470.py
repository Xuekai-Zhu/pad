def solution():
     cost = 1200
     discount = 15
     total_discount = cost * (discount / 100)
     final_cost = cost - total_discount
     result = final_cost
     return result

print(solution())