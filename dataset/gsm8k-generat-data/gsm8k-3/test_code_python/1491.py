def solution():
    """Mr Julien's store has 400 marbles remaining after the previous day's sales. Twenty customers came into the store, and each bought 15 marbles. How many marbles remain in the store?"""
    # Define the starting number of marbles in the store
    starting_marbles = 400

    # Define the number of customers and the quantity of marbles each customer purchased
    num_customers = 20
    marble_per_customer = 15

    # Calculate the total number of marbles sold
    marbles_sold = num_customers * marble_per_customer

    # Calculate the remaining number of marbles
    remaining_marbles = starting_marbles - marbles_sold

    # Display the remaining number of marbles
    result = remaining_marbles
    return result

print(solution())