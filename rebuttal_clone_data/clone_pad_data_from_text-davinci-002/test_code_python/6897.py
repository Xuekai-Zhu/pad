def solution():
     weekly_wage = 100
     budget = weekly_wage / 2
     money_spent_on_food = 10
     money_left_for_tokens = budget - money_spent_on_food
     price_per_hour = 8
     minutes_per_hour = 60
     tokens_per_hour = price_per_hour / minutes_per_hour
     minutes_of_playtime = money_left_for_tokens / tokens_per_hour
     result = minutes_of_playtime
     return result

print(solution())