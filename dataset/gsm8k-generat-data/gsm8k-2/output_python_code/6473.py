def solution():
    """Two companies A and B, are selling bottled milk. Company A sells a big bottle for $4 and Company B sells a big bottle for $3.5. Company A was able to sell 300 and company B 350 big bottles of milk. How much more money did one company make from the other?"""
    a_price = 4
    b_price = 3.5
    a_sold = 300
    b_sold = 350
    a_total_earnings = a_price * a_sold
    b_total_earnings = b_price * b_sold
    difference = abs(a_total_earnings - b_total_earnings)
    result = difference
    return result

print(solution())