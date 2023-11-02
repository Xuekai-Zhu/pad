def solution():
     pin_cost = 20
     percent_discount = 15
     discount_amount = pin_cost * (percent_discount / 100)
     cost_after_discount = pin_cost - discount_amount
     total_cost = cost_after_discount * 10
     result = total_cost
     return result

print(solution())