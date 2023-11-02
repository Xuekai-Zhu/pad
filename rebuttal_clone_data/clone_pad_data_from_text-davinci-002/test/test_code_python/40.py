def solution():
     
     crafts_sold = 3
     craft_price = 12
     extra_money = 7
     total_money = crafts_sold * craft_price + extra_money
     deposit = 18
     money_left = total_money - deposit
     result = money_left
     return result

print(solution())