def solution():
    """Brandon sold some geckos to a local pet shop. Brandon sold the geckos for 100$. 
    The pet store sells them for 5 more than 3 times that. How much does the pet store profit?"""
    
    # Calculate the selling price of the geckos by the pet store
    selling_price = 3 * 100 + 5

    # Calculate the profit per gecko
    profit_per_gecko = selling_price - 100

    # Assume that the pet store bought 'x' number of geckos from Brandon
    x = 10

    # Calculate the total profit
    total_profit = x * profit_per_gecko

    # Display the total profit
    result = total_profit
    return result

print(solution())