def solution():
    """If Patty's dress was $10 more than Ida's dress, and Ida's dress was $30 more than Jean's dress, and Jean's dress was $10 less than Pauline's dress, and lastly Pauline's dress was $30, how much did all the ladies spend on dressed put together?"""
    # Define the price of Pauline's dress
    PAULINE_PRICE = 30

    # Calculate the price of Jean's dress
    JEAN_PRICE = PAULINE_PRICE - 10

    # Calculate the price of Ida's dress
    IDA_PRICE = JEAN_PRICE + 30

    # Calculate the price of Patty's dress
    PATTY_PRICE = IDA_PRICE + 10

    # Calculate the total price of all the dresses
    total_price = PAULINE_PRICE + JEAN_PRICE + IDA_PRICE + PATTY_PRICE

    # Display the total price
    result = total_price
    return result

print(solution())