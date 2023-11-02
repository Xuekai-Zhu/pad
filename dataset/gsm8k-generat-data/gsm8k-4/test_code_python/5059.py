def solution():
    """James decides to sell 80% of his toys. He bought them for $20 each and sells them for $30 each. If he had 200 toys how much more money did he have compared to before he bought them?"""
    
    # Define the initial number of toys and the buy/sell prices
    num_toys = 200
    buy_price = 20
    sell_price = 30
    
    # Calculate the total money spent to buy the toys
    cost_price = num_toys * buy_price
    
    # Calculate the number of toys to be sold and the total money earned from selling them
    num_sold = int(num_toys * 0.8)
    sale_earnings = num_sold * sell_price
    
    # Calculate the net profit
    net_profit = sale_earnings - cost_price
    
    return net_profit

print(solution())