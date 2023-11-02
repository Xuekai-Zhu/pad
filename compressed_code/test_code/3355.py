def solution():
    
    cost_per_dozen = 5
    total_cost = 15
    rolls_per_dozen = 12
    dozens_purchased = total_cost / cost_per_dozen
    rolls_purchased = dozens_purchased * rolls_per_dozen
    result = rolls_purchased
    return result

print(solution())