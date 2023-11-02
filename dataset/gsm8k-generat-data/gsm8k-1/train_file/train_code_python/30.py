def solution():
    """Noah is a painter. He paints pictures and sells them at the park. He charges $60 for a large painting and $30 for a small painting. Last month he sold eight large paintings and four small paintings. If he sold twice as much this month, how much is his sales for this month?"""
    large_price = 60
    small_price = 30
    last_month_sales = 8*large_price + 4*small_price
    this_month_sales = last_month_sales * 2
    result = this_month_sales
    return result

print(solution())