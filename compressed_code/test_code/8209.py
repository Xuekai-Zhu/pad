def solution():
    
    total_paid = 20
    change_received = 11
    total_cost = total_paid - change_received
    cost_per_muffin = 0.75
    muffins_bought = total_cost / cost_per_muffin
    result = muffins_bought
    return result

print(solution())