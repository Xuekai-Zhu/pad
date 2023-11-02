def solution():
    """John goes to the store and pays with a 20 dollar bill. He buys 3 sodas and gets $14 in change. How much did each soda cost?"""
    bill_amount = 20
    sodas_bought = 3
    total_change = 14
    total_spent = bill_amount - total_change
    soda_cost = total_spent / sodas_bought
    result = soda_cost
    return result

print(solution())