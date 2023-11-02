def solution():
    """In the cafeteria, Athena wants to buy snacks for her friends. She bought 3 sandwiches at $3 each and 2 fruit drinks at $2.5 each. How much did she spend in all?"""
    # Define the cost of each item
    SANDWICH_PRICE = 3
    FRUIT_DRINK_PRICE = 2.5

    # Define the number of each item purchased
    sandwiches = 3
    fruit_drinks = 2

    # Calculate the total cost
    total_cost = (sandwiches * SANDWICH_PRICE) + (fruit_drinks * FRUIT_DRINK_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())