def solution():
    """Jack collects all his neighbors' recycling and sorts out the cans and bottles to return for the deposit. He gets 10 cents per bottle and 5 cents per can. If he recycled 80 bottles and made $15, how many cans did he recycle?"""
    # Define the prices and quantities
    bottle_price = 0.1
    can_price = 0.05
    bottle_qty = 80
    total_amount = 15

    # Calculate the total earnings from the bottles
    bottle_earnings = bottle_qty * bottle_price

    # Calculate the earnings from the cans
    can_earnings = total_amount - bottle_earnings

    # Calculate the number of cans recycled
    can_qty = int(can_earnings / can_price)

    # Return the result
    result = can_qty
    return result

print(solution())