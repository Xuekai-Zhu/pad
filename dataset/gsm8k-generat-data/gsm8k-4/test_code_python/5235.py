def solution():
    """Mr. Banks and Ms. Elizabeth are entrepreneurs who invest in different income streams and earn revenue from the investments. From each of his eight investments, Mr. Banks received $500 in revenue. Ms. Elizabeth also received $900 from each of her 5 investment streams. How much more money did Ms. Elizabeth make from her investments than Mr. Banks?"""
    # Calculate total revenue for Mr. Banks
    banks_revenue = 8 * 500

    # Calculate total revenue for Ms. Elizabeth
    elizabeth_revenue = 5 * 900

    # Calculate the difference in revenue
    revenue_diff = elizabeth_revenue - banks_revenue

    # Return the result
    result = revenue_diff
    return result

print(solution())