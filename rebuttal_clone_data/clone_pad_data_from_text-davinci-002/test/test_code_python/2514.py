def solution():
    cost = 50.00
    percent_entrees = 80
    entree_cost = cost * (percent_entrees / 100)
    appetizer_cost = cost - entree_cost
    appetizer_price = appetizer_cost / 2
    result = appetizer_price
    
    return result

print(solution())