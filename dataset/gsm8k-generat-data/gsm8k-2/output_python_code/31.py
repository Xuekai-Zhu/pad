def solution():
    """Noah is a painter. He paints pictures and sells them at the park. He charges $60 for a large painting and $30 for a small painting. Last month he sold eight large paintings and four small paintings. If he sold twice as much this month, how much is his sales for this month?"""
    large_price = 60
    small_price = 30
    last_month_large = 8
    last_month_small = 4
    this_month_large = last_month_large * 2
    this_month_small = last_month_small * 2
    total_sales = (this_month_large * large_price) + (this_month_small * small_price)
    result = total_sales
    return result

print(solution())