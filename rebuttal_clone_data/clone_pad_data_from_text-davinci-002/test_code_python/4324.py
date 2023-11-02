def solution():
     carmela_money = 7
     cousins_money = 2
     cousins_total = cousins_money * 4
     carmela_total = carmela_money + cousins_total
     carmela_average = carmela_total / 5
     money_to_give = carmela_average - carmela_money
     result = money_to_give
     return result

print(solution())