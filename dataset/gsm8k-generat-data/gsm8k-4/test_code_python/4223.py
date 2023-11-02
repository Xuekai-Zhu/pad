def solution():
    """Marcia wants to buy some fruit. Apples cost $2, bananas cost $1, and oranges cost $3. If Marcia buys 12 apples, 4 bananas and 4 oranges, what is the average cost of each piece of fruit in dollars?"""
    # Define the price of each type of fruit
    APPLE_PRICE = 2
    BANANA_PRICE = 1
    ORANGE_PRICE = 3

    # Define the quantity of each type of fruit purchased
    apples = 12
    bananas = 4
    oranges = 4

    # Calculate the total cost of the fruit
    total_cost = apples * APPLE_PRICE + bananas * BANANA_PRICE + oranges * ORANGE_PRICE

    # Calculate the total quantity of fruit purchased
    total_quantity = apples + bananas + oranges

    # Calculate the average cost of each piece of fruit
    average_cost = total_cost / total_quantity

    # Return the result
    result = average_cost
    return result

print(solution())