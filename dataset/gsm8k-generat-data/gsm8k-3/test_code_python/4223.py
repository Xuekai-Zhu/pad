def solution():
    """Marcia wants to buy some fruit. Apples cost $2, bananas cost $1, and oranges cost $3. If Marcia buys 12 apples, 4 bananas and 4 oranges, what is the average cost of each piece of fruit in dollars?"""
    # Define the prices per piece of fruit
    APPLE_PRICE = 2
    BANANA_PRICE = 1
    ORANGE_PRICE = 3

    # Define the quantities purchased for each type of fruit
    apple_qty = 12
    banana_qty = 4
    orange_qty = 4

    # Calculate the total cost of each type of fruit
    apple_cost = apple_qty * APPLE_PRICE
    banana_cost = banana_qty * BANANA_PRICE
    orange_cost = orange_qty * ORANGE_PRICE

    # Calculate the total cost of all the fruit
    total_cost = apple_cost + banana_cost + orange_cost

    # Calculate the average cost per piece of fruit
    total_qty = apple_qty + banana_qty + orange_qty
    avg_cost = total_cost / total_qty

    # Display the average cost per piece of fruit
    result = avg_cost
    return result

print(solution())