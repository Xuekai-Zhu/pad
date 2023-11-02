def solution():
    """Janet bought some muffins at the bakery. Each muffin is 75 cents. Janet paid $20 and got $11 in change back. How many muffins did Janet buy?"""
    total_paid = 20
    total_change = 11
    muffin_price = 0.75
    total_muffins = (total_paid - total_change) / muffin_price
    result = total_muffins
    return result

print(solution())