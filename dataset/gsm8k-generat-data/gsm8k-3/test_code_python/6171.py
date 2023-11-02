def solution():
    """Ted needs to purchase 5 bananas and 10 oranges.  If bananas cost $2 each and oranges cost $1.50 each.  How much money does Ted need to purchase 5 bananas and 10 oranges?"""
    # Define the cost of bananas and oranges
    BANANA_PRICE = 2
    ORANGE_PRICE = 1.5

    # Define the quantities of bananas and oranges
    bananas = 5
    oranges = 10

    # Calculate the total cost
    total_cost = bananas * BANANA_PRICE + oranges * ORANGE_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())