def solution():
    """Louise is in a toy store. She already has 28 toys worth $10 each in her cart. On her way to the till she adds 20 teddy bears to the cart. If the $580 in Louise’s wallet is exactly enough to pay for all the toys, how much does each teddy bear cost?"""
    toy_price = 10
    total_toys = 28
    teddy_bear_count = 20
    total_price = (toy_price * total_toys) + (teddy_bear_count * teddy_bear_price)
    wallet_amount = 580
    teddy_bear_price = (wallet_amount - total_price) / teddy_bear_count
    result = teddy_bear_price
    return result

print(solution())