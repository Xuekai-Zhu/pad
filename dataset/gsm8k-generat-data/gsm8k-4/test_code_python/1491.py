def solution():
    """Mr Julien's store has 400 marbles remaining after the previous day's sales. Twenty customers came into the store, and each bought 15 marbles. How many marbles remain in the store?"""
    # Define the initial number of marbles
    initial_marbles = 400

    # Define the number of customers and the number of marbles sold per customer
    num_customers = 20
    marbles_per_customer = 15

    # Calculate the total number of marbles sold
    total_marbles_sold = num_customers * marbles_per_customer

    # Calculate the remaining number of marbles
    remaining_marbles = initial_marbles - total_marbles_sold

    # return the result
    result = remaining_marbles
    return result

print(solution())