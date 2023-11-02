def solution():
    """Sofia and her mother go to the grocery store and buys 10kgs of oranges to be used in their home for the week. While at the store, Sofia's father calls and says they're to add 5 more kgs since their neighbor also wanted some supplies. When they reach home, they estimated that for the next coming two weeks they'll have to buy twice as many oranges each week for the supplies to be enough. What the total quantity of oranges they would have bought after the three weeks."""
    # Define the initial quantity of oranges purchased
    initial_quantity = 10

    # Define the quantity of oranges to be added for the neighbor
    neighbor_quantity = 5

    # Determine the new quantity of oranges for the first week
    total_quantity = initial_quantity + neighbor_quantity

    # Determine the quantity of oranges for the next two weeks
    doubled_quantity = total_quantity * 2

    # Calculate the total quantity of oranges purchased
    total_oranges = total_quantity + doubled_quantity

    # Return the result
    result = total_oranges
    return result

print(solution())