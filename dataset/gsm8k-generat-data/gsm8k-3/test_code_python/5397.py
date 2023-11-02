def solution():
    """Grant decided to sell his baseball gear since he was now playing football. He sold his baseball cards for $25. He got $10 for his baseball bat and agreed to sell his $30 baseball glove at 20% off. He also sold both pair of his baseball cleats for $10 each. How much money did Grant make?"""
    # Calculate the amount earned from selling baseball cards
    cards_price = 25

    # Calculate the amount earned from selling baseball bat
    bat_price = 10

    # Calculate the amount earned from selling baseball glove with a 20% discount
    glove_price = 30 * 0.8

    # Calculate the amount earned from selling both pairs of baseball cleats
    cleats_price = 2 * 10

    # Calculate the total amount earned
    total_earnings = cards_price + bat_price + glove_price + cleats_price

    # Return the total amount earned
    result = total_earnings
    return result

print(solution())