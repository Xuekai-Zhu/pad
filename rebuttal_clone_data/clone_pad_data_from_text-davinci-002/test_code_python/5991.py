def solution():
     initial_balance = 125
     increase_percent = 25
     decrease_percent = 20
     increase_amount = initial_balance * (increase_percent / 100)
     decrease_amount = increase_amount * (decrease_percent / 100)
     final_balance = initial_balance + increase_amount - decrease_amount
     final_balance_percent = final_balance / initial_balance * 100
     result = final_balance_percent
     return result

print(solution())