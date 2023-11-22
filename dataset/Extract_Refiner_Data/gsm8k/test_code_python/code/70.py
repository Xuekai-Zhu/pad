def solution():
    
    marigold_price = 2.74
    petunia_price = 1.87
    begonia_price = 2.12
    marigold_pots = 12
    petunia_pots = 9
    begonia_pots = 17
    total_price = (marigold_price * marigold_pots) + (petunia_price * petunia_pots) + (begonia_price * begonia_pots)
    rounded_price = round(total_price)
    result = rounded_price
    return result

print(solution())