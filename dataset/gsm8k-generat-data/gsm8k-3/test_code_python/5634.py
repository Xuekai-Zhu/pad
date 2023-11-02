def solution():
    """An author of a book got 6% of the total sales of the paper cover version of his books and 12% of the total sales of the hardcover version. If 32,000 copies of the paper cover version were sold at $0.20 each and 15,000 copies of the hardcover version were sold at $0.40 each, how much did the author earn?"""
    # Define the sales and commission rates for the paper and hardcover versions
    PAPER_SALES = 32000
    HARDCOVER_SALES = 15000
    PAPER_PRICE = 0.20
    HARDCOVER_PRICE = 0.40
    PAPER_COMMISSION = 0.06
    HARDCOVER_COMMISSION = 0.12

    # Calculate the author's earnings from the paper version
    paper_earnings = PAPER_SALES * PAPER_PRICE * PAPER_COMMISSION

    # Calculate the author's earnings from the hardcover version
    hardcover_earnings = HARDCOVER_SALES * HARDCOVER_PRICE * HARDCOVER_COMMISSION

    # Calculate the total earnings of the author
    total_earnings = paper_earnings + hardcover_earnings

    # Display the author's earnings
    result = total_earnings
    return result

print(solution())