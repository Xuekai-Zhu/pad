def solution():
    """Michael loves to paint and sells his creations. He charges $100 for a large painting and $80 for a small painting. At his last art show, he sold 5 large paintings and 8 small paintings. How much did he earn in all?"""
    large_price = 100
    small_price = 80
    num_large_paintings = 5
    num_small_paintings = 8
    total_money = (large_price * num_large_paintings) + (small_price * num_small_paintings)
    result = total_money
    return result

print(solution())