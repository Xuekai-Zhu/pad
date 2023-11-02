def solution():
     chores_per_week = 4
     cookies_per_chore = 3
     money = 15
     price_per_package = 3
     cookies_per_package = 24
     number_of_weeks = money // (price_per_package + (chores_per_week * cookies_per_chore))
     result = number_of_weeks
     return result

print(solution())