def solution():
    """John sells 20 woodburning for $15 each.  The wood cost $100.  How much does he make in profit?"""
    # Define the cost of the wood
    wood_cost = 100
    
    # Define the price of each woodburning
    price = 15
    
    # Define the number of woodburnings sold
    quantity = 20
    
    # Calculate the total revenue
    revenue = price * quantity
    
    # Calculate the profit
    profit = revenue - wood_cost
    
    # Display the profit
    result = profit
    return result

print(solution())