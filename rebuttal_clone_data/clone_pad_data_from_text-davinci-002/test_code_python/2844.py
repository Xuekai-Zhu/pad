def solution():
     current_dolls = 100
     new_dolls = 2
     percent_increase = 25
     increase_amount = current_dolls * (percent_increase / 100)
     total_dolls = current_dolls + new_dolls + increase_amount
     result = total_dolls
     
     return result

print(solution())