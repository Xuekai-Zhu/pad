def solution():
    num_large_paintings = 8
    large_painting_price = 60

    num_small_paintings = 4
    small_painting_price = 30

    # Calculate the total sales from last month
    total_sales_last_month = (num_large_paintings * large_painting_price) + (num_small_paintings * small_painting_price)

    # Calculate the total number of paintings sold this month
    total_paintings_this_month = (2 * num_large_paintings) + (2 * num_small_paintings)

    # Calculate the total sales for this month
    total_sales_this_month = (total_paintings_this_month - num_large_paintings - num_small_paintings) * large_painting_price \
                             + num_large_paintings * (large_painting_price * 0.8) \
                             + num_small_paintings * (small_painting_price * 0.8)
    result = total_sales_this_month
    return result

print(solution())