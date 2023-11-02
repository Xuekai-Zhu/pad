def solution():
    """James is running a fundraiser selling candy bars. Each box has 10 candy bars in it. He sells 5 boxes. 
    He sells each candy bar for $1.50 and buys each bar for $1. How much profit does he make from these sales?"""
    # Define the cost and selling price of each candy bar
    cost_per_bar = 1
    selling_price_per_bar = 1.5

    # Calculate the profit per box
    profit_per_box = (selling_price_per_bar - cost_per_bar) * 10

    # Calculate the total profit from selling 5 boxes
    total_profit = profit_per_box * 5

    result = total_profit
    return result

print(solution())