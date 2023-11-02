def solution():
    """Will's mom gave him $74 to go shopping. He bought a sweater for $9, a T-shirt for $11 and a pair of shoes for $30. He then returned his shoes for a 90% refund.  How much money does Will have left?"""
    # Define the prices of the items
    SWEATER_PRICE = 9
    T_SHIRT_PRICE = 11
    SHOES_PRICE = 30

    # Define the amount of money Will was given and spent
    total_money = 74
    spent_money = SWEATER_PRICE + T_SHIRT_PRICE + SHOES_PRICE

    # Calculate the amount of money Will gets back for the shoes
    returned_money = SHOES_PRICE * 0.9

    # Calculate the total amount of money Will has left
    remaining_money = total_money - spent_money + returned_money

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())