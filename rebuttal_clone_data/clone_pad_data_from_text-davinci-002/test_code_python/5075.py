def solution():
     discount = 10
     total_cost = 250
     final_cost = total_cost - (total_cost * (discount/100))
     result = final_cost
     return result

print(solution())