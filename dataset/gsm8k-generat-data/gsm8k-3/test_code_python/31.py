def solution():
    """Noah is a painter. He paints pictures and sells them at the park. He charges $60 for a large painting and $30 for a small painting. Last month he sold eight large paintings and four small paintings. If he sold twice as much this month, how much is his sales for this month?"""
    # Define the prices of a large and small painting
    large_price = 60
    small_price = 30

    # Define the number of large and small paintings sold last month
    large_count_last_month = 8
    small_count_last_month = 4

    # Calculate the total sales last month
    sales_last_month = (large_count_last_month * large_price) + (small_count_last_month * small_price)

    # Calculate the number of large and small paintings sold this month
    large_count_this_month = large_count_last_month * 2
    small_count_this_month = small_count_last_month * 2

    # Calculate the total sales this month
    sales_this_month = (large_count_this_month * large_price) + (small_count_this_month * small_price)

    # return the result
    result = sales_this_month
    return result

print(solution())