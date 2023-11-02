def solution():
    """James decides to sell 80% of his toys.  He bought them for $20 each and sells them for $30 each. If he had 200 toys how much more money did he have compared to before he bought them?"""
    # Define the number of toys and the cost per toy
    NUM_TOYS = 200
    COST_PER_TOY = 20

    # Calculate the total cost of all the toys
    total_cost = NUM_TOYS * COST_PER_TOY

    # Calculate the number of toys James will sell
    num_toys_sold = NUM_TOYS * 0.8

    # Calculate the total revenue from selling the toys
    revenue = num_toys_sold * 30

    # Calculate the profit made from selling the toys
    profit = revenue - total_cost

    # Display the profit made
    result = profit
    return result

print(solution())