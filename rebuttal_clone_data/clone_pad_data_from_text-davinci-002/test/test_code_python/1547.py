def solution():
     goal_amount = 485
     money_given = 250
     money_needed = goal_amount - money_given
     price_per_candy_bar = 1.25
     candy_bars_needed = money_needed / price_per_candy_bar
     result = candy_bars_needed
     return result

print(solution())