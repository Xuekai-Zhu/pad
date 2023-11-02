def solution():
    
    total_cost = 50
    entree_cost = total_cost * 0.8 / 4
    appetizer_cost = (total_cost - entree_cost * 4) / 2
    result = appetizer_cost
    return result

print(solution())