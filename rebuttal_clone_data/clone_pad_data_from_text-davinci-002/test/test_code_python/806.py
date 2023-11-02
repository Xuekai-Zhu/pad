def solution():
     bottle_price = 50
     money_saved_c = 5
     money_saved_s = 7
     money_earned_c = 20
     money_earned_s = 12
     
     total_money_saved = money_saved_c + money_saved_s
     total_money_earned = money_earned_c + money_earned_s
     
     money_needed = bottle_price - (total_money_saved + total_money_earned)
     result = money_needed
     
     return result

print(solution())