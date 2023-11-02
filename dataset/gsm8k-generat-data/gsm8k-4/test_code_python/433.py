def solution():
    """Michael loves to paint and sells his creations. He charges $100 for a large painting and $80 for a small painting. At his last art show, he sold 5 large paintings and 8 small paintings. How much did he earn in all?"""
    # Define the prices of a large and a small painting
    large_price = 100
    small_price = 80

    # Define the number of sold paintings
    num_large = 5
    num_small = 8

    # Calculate the total earnings
    total_earnings = (num_large * large_price) + (num_small * small_price)

    result = total_earnings
    return result

print(solution())