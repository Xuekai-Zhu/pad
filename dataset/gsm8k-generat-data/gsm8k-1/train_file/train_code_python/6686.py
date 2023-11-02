def solution():
    """
    John goes to the store and pays with a 20 dollar bill. He buys 3 sodas and gets $14 in change. How much did each soda cost?
    """
    bill = 20
    sodas = 3
    change = 14
    total_cost = bill - change
    cost_per_soda = total_cost / sodas
    result = cost_per_soda
    
    return result

print(solution())