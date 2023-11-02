def solution():
    """Lucas went to the store with $20 and needed to buy 3 avocados that cost $2 each. How much change does he bring home?"""
    # Define the cost of each avocado
    AVOCADO_PRICE = 2

    # Define the number of avocados to be purchased
    avocados = 3

    # Calculate the total cost of the avocados
    total_cost = avocados * AVOCADO_PRICE

    # Calculate the amount of change Lucas brings home
    change = 20 - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())