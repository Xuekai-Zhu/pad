def solution():
     water_cost = 4 * 2
     cheese_cost = 10 + (10 / 2)
     total_cost = water_cost + cheese_cost
     money_remaining = 100 - total_cost
     result = money_remaining
     return result

print(solution())