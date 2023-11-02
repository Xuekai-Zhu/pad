def solution():
    """Grant decided to sell his baseball gear since he was now playing football. He sold his baseball cards for $25. He got $10 for his baseball bat and agreed to sell his $30 baseball glove at 20% off. He also sold both pair of his baseball cleats for $10 each. How much money did Grant make?"""

    # Calculate the total amount earned from selling baseball cards, bat, and cleats
    total_sale = 25 + 10 + (2 * 10)

    # Calculate the discounted price of the baseball glove
    glove_discounted_price = 30 - (30 * 0.2)

    # Add the amount earned from selling the glove to the total sale
    total_sale += glove_discounted_price

    result = total_sale
    return result

print(solution())