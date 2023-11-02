def solution():
     cost_per_kilogram = 5
     discount_percentage = 40
     discount_amount = cost_per_kilogram * (discount_percentage / 100)
     cost_after_discount = cost_per_kilogram - discount_amount
     total_cost = cost_after_discount * 10
     result = total_cost
     return result

print(solution())