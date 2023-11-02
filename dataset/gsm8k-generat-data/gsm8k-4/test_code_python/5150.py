def solution():
    """Paul went to the sporting goods store to buy a tennis racket. His favorite brand was having a sale that offered customers a deal to buy one racket at full price and get the second racket for half off the full price. If he purchased two rackets that were each originally marked at a full price of $60, how much did he spend on the two rackets, in dollars?"""
    
    # Calculate the full price of two rackets
    full_price = (2 * 60)

    # Calculate the price of the second racket at half off the full price
    half_price = (60 / 2)

    # Calculate the total cost of the two rackets with the sale
    total_cost = (full_price - half_price)

    result = total_cost
    return result

print(solution())