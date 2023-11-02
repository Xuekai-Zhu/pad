def solution():
     
     money_earned = [18, 9, 20]
     money_needed = 60
     total_money_earned = sum(money_earned)
     money_needed = money_needed - total_money_earned
     result = money_needed
     return result

print(solution())