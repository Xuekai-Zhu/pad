def solution():
    """Mr. Banks and Ms. Elizabeth are entrepreneurs who invest in different income streams and earn revenue from the investments. From each of his eight investments, Mr. Banks received $500 in revenue. Ms. Elizabeth also received $900 from each of her 5 investment streams. How much more money did Ms. Elizabeth make from her investments than Mr. Banks?"""
    # Define the revenue per investment for Mr. Banks and Ms. Elizabeth
    BANKS_REVENUE_PER_INVESTMENT = 500
    ELIZABETH_REVENUE_PER_INVESTMENT = 900

    # Define the number of investments for Mr. Banks and Ms. Elizabeth
    NUM_BANKS_INVESTMENTS = 8
    NUM_ELIZABETH_INVESTMENTS = 5

    # Calculate the total revenue for Mr. Banks and Ms. Elizabeth
    banks_total_revenue = BANKS_REVENUE_PER_INVESTMENT * NUM_BANKS_INVESTMENTS
    elizabeth_total_revenue = ELIZABETH_REVENUE_PER_INVESTMENT * NUM_ELIZABETH_INVESTMENTS

    # Calculate the difference between their total revenues
    revenue_difference = elizabeth_total_revenue - banks_total_revenue

    # Display the difference in revenue
    result = revenue_difference
    return result

print(solution())