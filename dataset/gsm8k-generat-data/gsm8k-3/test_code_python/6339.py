def solution():
    """Sofia and her mother go to the grocery store and buys 10kgs of oranges to be used in their home for the week. While at the store, Sofia's father calls and says they're to add 5 more kgs since their neighbor also wanted some supplies. When they reach home, they estimated that for the next coming two weeks they'll have to buy twice as many oranges each week for the supplies to be enough. What the total quantity of oranges they would have bought after the three weeks."""
    # Define the initial amount of oranges purchased
    initial_oranges = 10

    # Add the additional oranges for the neighbor
    total_oranges = initial_oranges + 5

    # Calculate the amount of oranges needed for the next two weeks
    additional_oranges = initial_oranges * 2

    # Add the additional oranges to the total amount
    total_oranges += additional_oranges * 2

    # Display the total amount of oranges
    result = total_oranges
    return result

print(solution())