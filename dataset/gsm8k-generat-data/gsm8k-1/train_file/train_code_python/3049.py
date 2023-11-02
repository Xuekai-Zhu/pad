def solution():
    """Janet bought some muffins at the bakery. Each muffin is 75 cents. Janet paid $20 and got $11 in change back. How many muffins did Janet buy?"""
    total_paid = 20
    change_received = 11
    total_cost = total_paid - change_received
    cost_per_muffin = 0.75
    muffins_bought = total_cost / cost_per_muffin
    result = muffins_bought
    return result

print(solution())