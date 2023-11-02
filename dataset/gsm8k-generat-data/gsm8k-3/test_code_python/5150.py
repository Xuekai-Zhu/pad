def solution():
    """Paul went to the sporting goods store to buy a tennis racket.  His favorite brand was having a sale that offered customers a deal to buy one racket at full price and get the second racket for half off the full price.   If he purchased two rackets that were each originally marked at a full price of $60, how much did he spend on the two rackets, in dollars?"""
    # Define the original price of a racket
    ORIGINAL_PRICE = 60

    # Calculate the discounted price of the second racket (half off the full price)
    discounted_price = ORIGINAL_PRICE / 2

    # Calculate the total cost of the two rackets
    total_cost = ORIGINAL_PRICE + discounted_price

    # Display the total cost
    result = total_cost
    return result

print(solution())