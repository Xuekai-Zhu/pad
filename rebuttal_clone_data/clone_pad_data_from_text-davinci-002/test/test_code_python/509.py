def solution():
     mold_cost = 250
     hour_cost = 75
     hours = 8
     work_cost = hour_cost * hours
     percent_discount = 20
     discount_amount = work_cost * (percent_discount / 100)
     final_cost = work_cost - discount_amount + mold_cost
     result = final_cost
     return result

print(solution())