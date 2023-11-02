def solution():
    """Blake goes to the grocery store and spends $40 on oranges, $50 on apples, and $60 on mangoes. If he has $300, how much change was he given?"""
    # Define the prices of each type of fruit
    ORANGE_PRICE = 40
    APPLE_PRICE = 50
    MANGO_PRICE = 60

    # Calculate the total amount spent on fruit
    total_spent = ORANGE_PRICE + APPLE_PRICE + MANGO_PRICE

    # Calculate the amount of change Blake was given
    change = 300 - total_spent

    # Display the change he was given
    result = change
    return result

print(solution())