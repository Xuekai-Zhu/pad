def solution():
     cost_per_pair = 10
     discount_percent = 10
     num_pairs = 3
     total_cost = cost_per_pair * num_pairs
     discount_amount = total_cost * (discount_percent / 100)
     final_cost_3pairs = total_cost - discount_amount
     final_cost_1pair = cost_per_pair
     savings = final_cost_1pair - final_cost_3pairs
     result = savings
     return result

print(solution())