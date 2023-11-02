def solution():
    """James is running a fundraiser selling candy bars. Each box has 10 candy bars in it. He sells 5 boxes. He sells each candy bar for $1.50 and buys each bar for $1. How much profit does he make from these sales?"""
    # Define the number of candy bars in a box
    BARS_PER_BOX = 10

    # Define the cost and selling price per candy bar
    COST_PER_BAR = 1
    SELLING_PRICE_PER_BAR = 1.5

    # Define the number of boxes sold
    boxes_sold = 5

    # Calculate the total cost of the candy bars
    total_cost = COST_PER_BAR * BARS_PER_BOX * boxes_sold

    # Calculate the total revenue from selling the candy bars
    total_revenue = SELLING_PRICE_PER_BAR * BARS_PER_BOX * boxes_sold

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())