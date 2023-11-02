def solution():
    
    total_paid = 20
    total_change = 11
    muffin_price = 0.75
    total_muffins = (total_paid - total_change) / muffin_price
    result = total_muffins
    return result

print(solution())