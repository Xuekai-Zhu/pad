def solution():
    """Michael loves to paint and sells his creations. He charges $100 for a large painting and $80 for a small painting. At his last art show, he sold 5 large paintings and 8 small paintings. How much did he earn in all?"""
    # Define the price of a large painting and a small painting
    LARGE_PRICE = 100
    SMALL_PRICE = 80

    # Define the number of each painting sold
    large_paintings_sold = 5
    small_paintings_sold = 8

    # Calculate the total earnings
    total_earnings = (large_paintings_sold * LARGE_PRICE) + (small_paintings_sold * SMALL_PRICE)

    # Display the total earnings
    result = total_earnings
    return result

print(solution())