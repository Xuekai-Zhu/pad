def solution():
     cost_per_loot_box = 5
     value_per_loot_box = 3.5
     total_cost = cost_per_loot_box * 40
     total_value = value_per_loot_box * 40
     average_loss = total_cost - total_value
     result = average_loss
     return result

print(solution())