def solution():
     initial_money = 65
     money_spent_on_ice_cream = 5
     money_spent_on_shirt = (initial_money - money_spent_on_ice_cream) / 2
     money_left = initial_money - money_spent_on_ice_cream - money_spent_on_shirt
     money_deposited = money_left / 5
     money_left_after_deposit = money_left - money_deposited
     result = money_left_after_deposit
     return result

print(solution())