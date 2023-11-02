def solution():
    """Two companies A and B, are selling bottled milk. Company A sells a big bottle for $4 and Company B sells a big bottle for $3.5. Company A was able to sell 300 and company B 350 big bottles of milk. How much more money did one company make from the other?"""
    price_a = 4
    price_b = 3.5
    sold_a = 300
    sold_b = 350
    total_income_a = price_a * sold_a
    total_income_b = price_b * sold_b
    difference = abs(total_income_a - total_income_b)
    result = difference
    return result

print(solution())