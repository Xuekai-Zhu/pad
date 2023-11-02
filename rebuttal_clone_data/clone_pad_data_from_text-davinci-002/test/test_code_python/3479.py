def solution():
     cost_of_gift = 250
     erika_saved = 155
     ricks_saved = cost_of_gift / 2
     total_saved = erika_saved + ricks_saved
     cost_of_cake = 25
     money_left = total_saved - (cost_of_gift + cost_of_cake)
     result = money_left
     return result

print(solution())