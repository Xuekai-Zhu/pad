def solution():
    """Michael loves to paint and sells his creations. He charges $100 for a large painting and $80 for a small painting. At his last art show, he sold 5 large paintings and 8 small paintings. How much did he earn in all?"""
    price_large = 100
    price_small = 80
    num_large = 5
    num_small = 8
    total_earned = (price_large*num_large) + (price_small*num_small)
    result = total_earned
    return result

print(solution())