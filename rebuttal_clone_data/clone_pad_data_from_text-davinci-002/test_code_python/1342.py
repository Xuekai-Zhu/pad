def solution():
     investment_per_week = 2000
     money_in_account = 250000
     percent_increase = 50
     increase_amount = money_in_account * (percent_increase / 100)
     total_money = money_in_account + investment_per_week + increase_amount
     result = total_money
     return result

print(solution())