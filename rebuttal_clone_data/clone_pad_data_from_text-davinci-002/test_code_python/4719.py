def solution():
     original_amount = 48
     final_amount = original_amount + 4
     half_amount = original_amount / 2
     money_left = final_amount - half_amount
     spent_on_accessories = money_left - 8
     result = spent_on_accessories
     return result

print(solution())