def solution():
    """Steve's new book sells 1,000,000 copies. He got an advance to pay for 100,000 copies. He gets $2 for each copy of the book sold. His agent takes 10% of that. How much money did he keep not counting the money from the advance?"""
    # Define the total number of copies sold and the price per copy
    total_copies_sold = 1000000
    price_per_copy = 2

    # Calculate the total revenue from selling all copies
    total_revenue = total_copies_sold * price_per_copy

    # Calculate the commission taken by the agent
    agent_commission = total_revenue * 0.1

    # Calculate the revenue Steve keeps after the agent's commission and the advance payment
    revenue = total_revenue - agent_commission - (100000 * price_per_copy)

    # return the result
    result = revenue
    return result

print(solution())