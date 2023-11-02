def solution():
    """Dennis wants to buy 4 pairs of pants from the store which cost $110.00 each with a 30% discount and he also wants to buy 2 pairs of socks which cost $60.00 with a 30% discount. How much money will Dennis have to spend in total after he bought all the items he wants after the discount?"""
    pants_price = 110.00
    pants_discount = 0.30
    socks_price = 60.00
    socks_discount = 0.30
    num_pants = 4
    num_socks = 2
    
    total_pants_price = pants_price * num_pants
    total_pants_discount = total_pants_price * pants_discount
    total_pants_after_discount = total_pants_price - total_pants_discount
    
    total_socks_price = socks_price * num_socks
    total_socks_discount = total_socks_price * socks_discount
    total_socks_after_discount = total_socks_price - total_socks_discount
    
    total_spent = total_pants_after_discount + total_socks_after_discount
    result = total_spent
    
    return result

print(solution())