def solution():
     monday_profit = 1/3
     tuesday_profit = 1/4
     wednesday_profit = 1 - monday_profit - tuesday_profit
     total_profit = 1200
     wednesday_earnings = total_profit * wednesday_profit
     
     return wednesday_earnings

print(solution())