def solution():
    """Adam went to a shop to buy some food for his journey. He bought 3 sandwiches, for $3 each, and a bottle of water for $2. How much did Adam pay for all the shopping?"""
    # Define the cost of each item
    SANDWICH_PRICE = 3
    WATER_PRICE = 2

    # Define the number of items purchased
    sandwiches = 3
    water = 1

    # Calculate the total cost
    total_cost = (sandwiches * SANDWICH_PRICE) + (water * WATER_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())