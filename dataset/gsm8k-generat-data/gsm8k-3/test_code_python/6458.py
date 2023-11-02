def solution():
    """Frank went to a shop to buy some food for his breakfast. He bought 10 buns for $0.1 each, two bottles of milk, for $2 each, and a carton of eggs, which was three times more expensive than one bottle of milk. How much did Frank pay for his breakfast shopping?"""
    # Define the cost of each item
    BUN_PRICE = 0.1
    MILK_PRICE = 2
    EGG_PRICE = 3 * MILK_PRICE

    # Define the quantity of each item purchased
    bun_quantity = 10
    milk_quantity = 2
    egg_quantity = 1

    # Calculate the total cost of buns
    bun_cost = bun_quantity * BUN_PRICE

    # Calculate the total cost of milk
    milk_cost = milk_quantity * MILK_PRICE

    # Calculate the total cost of eggs
    egg_cost = egg_quantity * EGG_PRICE

    # Calculate the total cost of breakfast shopping
    total_cost = bun_cost + milk_cost + egg_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())