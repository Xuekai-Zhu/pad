def solution():
    """John sells 20 woodburning for $15 each. The wood cost $100. How much does he make in profit?"""
    # Define the number of woodburning sold and their selling price
    num_woodburning = 20
    woodburning_price = 15

    # Define the cost of the wood
    wood_cost = 100

    # Calculate the total revenue from selling the woodburning
    total_revenue = num_woodburning * woodburning_price

    # Calculate the total cost of producing the woodburning
    total_cost = wood_cost + total_revenue

    # Calculate the profit
    profit = total_revenue - total_cost

    # Return the profit
    result = profit
    return result

print(solution())