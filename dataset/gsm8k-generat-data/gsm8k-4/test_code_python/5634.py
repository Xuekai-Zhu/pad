def solution():
    """An author of a book got 6% of the total sales of the paper cover version of his books and 12% of the total sales of the hardcover version. If 32,000 copies of the paper cover version were sold at $0.20 each and 15,000 copies of the hardcover version were sold at $0.40 each, how much did the author earn?"""
    # Calculate the earnings from the paper cover version
    paper_sales = 32000 * 0.20 * 0.06

    # Calculate the earnings from the hardcover version
    hardcover_sales = 15000 * 0.40 * 0.12

    # Calculate the total earnings
    total_earnings = paper_sales + hardcover_sales

    # Return the result
    result = total_earnings
    return result

print(solution())