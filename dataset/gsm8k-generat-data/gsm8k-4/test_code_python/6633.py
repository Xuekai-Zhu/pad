def solution():
    """Dennis wants to buy 4 pairs of pants from the store which cost $110.00 each with a 30% discount and he also wants to buy 2 pairs of socks which cost $60.00 with a 30% discount. How much money will Dennis have to spend in total after he bought all the items he wants after the discount?"""
    # Define the prices of pants and socks before discount
    pants_price = 110.00
    socks_price = 60.00

    # Apply the discount to the prices
    pants_discount = pants_price * 0.30
    socks_discount = socks_price * 0.30
    pants_price -= pants_discount
    socks_price -= socks_discount

    # Calculate the total cost of all items
    total_cost = 4*pants_price + 2*socks_price

    result = total_cost
    return result

print(solution())