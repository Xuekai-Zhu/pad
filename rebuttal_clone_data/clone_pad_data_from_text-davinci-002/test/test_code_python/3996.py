def solution():
     cost_per_balloon = 0.5
     pack_cost = 3
     balloon_amount = 14
     remainder = balloon_amount % 10
     pack_amount = (balloon_amount - remainder) / 10
     total_cost = (pack_amount * pack_cost) + (remainder * cost_per_balloon)
     result = total_cost
     return result

print(solution())