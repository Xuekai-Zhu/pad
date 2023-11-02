def solution():
    """Noah is a painter. He paints pictures and sells them at the park. He charges $60 for a large painting and $30 for a small painting. Last month he sold eight large paintings and four small paintings. If he sold twice as much this month, how much is his sales for this month?"""
    # Define the prices and quantities of paintings sold last month
    large_price = 60
    small_price = 30
    last_month_large_qty = 8
    last_month_small_qty = 4

    # Calculate the total sales from last month
    last_month_sales = (large_price * last_month_large_qty) + (small_price * last_month_small_qty)

    # Calculate the quantities sold this month
    this_month_large_qty = last_month_large_qty * 2
    this_month_small_qty = last_month_small_qty * 2

    # Calculate the total sales for this month
    this_month_sales = (large_price * this_month_large_qty) + (small_price * this_month_small_qty)

    result = this_month_sales
    return result

print(solution())