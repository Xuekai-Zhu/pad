def solution():
     slurpees_cost = 2
     money_given = 20
     money_received = 8
     total_cost = money_given - money_received
     slurpees_bought = total_cost // slurpees_cost
     result = slurpees_bought
     return result

print(solution())