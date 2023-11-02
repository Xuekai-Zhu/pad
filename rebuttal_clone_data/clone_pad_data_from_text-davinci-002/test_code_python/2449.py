def solution():
     shirts_bought = 10
     sandals_bought = 3
     shirt_cost = 5
     sandal_cost = 3
     total_cost = shirt_cost * shirts_bought + sandal_cost * sandals_bought
     money_given = 100
     change = money_given - total_cost
     result = change
     return result

print(solution())