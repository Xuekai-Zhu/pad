def solution():
    
    cost_per_dozen = 5
    total_cost = 15
    dozens_purchased = total_cost // cost_per_dozen
    rolls_purchased = dozens_purchased * 12
    result = rolls_purchased
    return result

print(solution())