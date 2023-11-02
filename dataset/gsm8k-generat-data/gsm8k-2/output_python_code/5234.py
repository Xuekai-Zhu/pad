def solution():
    """Mr. Banks and Ms. Elizabeth are entrepreneurs who invest in different income streams and earn revenue from the investments. From each of his eight investments, Mr. Banks received $500 in revenue. Ms. Elizabeth also received $900 from each of her 5 investment streams. How much more money did Ms. Elizabeth make from her investments than Mr. Banks?"""
    banks_revenue = 500 * 8
    elizabeth_revenue = 900 * 5
    difference = elizabeth_revenue - banks_revenue
    result = difference
    return result

print(solution())