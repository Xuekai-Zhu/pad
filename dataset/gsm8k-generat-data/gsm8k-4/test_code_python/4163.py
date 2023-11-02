def solution():
    """Tom buys 20 shares of a stock that costs $3 each. He sells 10 of those shares for $4 each. The rest of the shares end up doubling in value. How much profit does he make?"""
    
    # Define the number of shares and the price per share
    SHARES = 20
    PRICE_PER_SHARE = 3
    
    # Define the number of shares sold and the selling price per share
    SHARES_SOLD = 10
    SELLING_PRICE = 4
    
    # Calculate the total cost of buying the shares
    total_cost = SHARES * PRICE_PER_SHARE
    
    # Calculate the earnings from selling the shares
    earnings = SHARES_SOLD * SELLING_PRICE
    
    # Calculate the remaining shares and the total earnings from selling them
    remaining_shares = SHARES - SHARES_SOLD
    remaining_earnings = remaining_shares * PRICE_PER_SHARE * 2
    
    # Calculate the total profit
    total_profit = earnings + remaining_earnings - total_cost
    
    # Return the result
    return total_profit

print(solution())