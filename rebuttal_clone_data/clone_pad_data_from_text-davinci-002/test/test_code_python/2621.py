def solution():
     ounces_sold = 8
     ounces_confiscated = 1
     price_per_ounce = 9
     total_money = ounces_sold * price_per_ounce
     fine = 50
     money_left = total_money - fine
     result = money_left
 
     return result

print(solution())