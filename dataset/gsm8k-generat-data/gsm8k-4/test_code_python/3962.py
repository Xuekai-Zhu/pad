def solution():
    """Lucas went to the store with $20 and needed to buy 3 avocados that cost $2 each. How much change does he bring home?"""
    # Define the cost of each avocado and the number of avocados needed
    avocado_cost = 2
    num_avocados = 3

    # Define the amount of money Lucas brought to the store
    money_brought = 20

    # Calculate the total cost of the avocados
    total_cost = avocado_cost * num_avocados

    # Calculate the amount of change Lucas brings home
    change = money_brought - total_cost

    # Return the result
    result = change
    return result

print(solution())