def solution():
    """David found $12 on the street. He then gave it to his friend Evan who has $1 and needed to buy a watch worth $20. How much does Evan still need?"""
    # Define the initial amount of money David found
    initial_amount = 12

    # Define Evan's starting amount of money and the cost of the watch
    evan_amount = 1
    watch_cost = 20

    # Add the amount David found to Evan's starting amount
    evan_amount += initial_amount

    # Subtract the cost of the watch from Evan's total amount of money
    evan_amount -= watch_cost

    # Calculate how much money Evan still needs
    still_needs = -evan_amount

    # Return the result
    result = still_needs
    return result

print(solution())