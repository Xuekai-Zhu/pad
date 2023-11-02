def solution():
    # Calculate the total amount from selling baseball cards, bat, and cleats
    total_amount = 25 + 10 + (10 * 2)  # $25 for cards, $10 for bat, $10 each for 2 pairs of cleats

    # Calculate the discounted price of the baseball glove
    discounted_price = 30 * 0.2  # 20% off of $30
    glove_price = 30 - discounted_price

    # Add the amount from selling the glove to the total amount
    total_amount += glove_price

    result = total_amount
    return result

print(solution())