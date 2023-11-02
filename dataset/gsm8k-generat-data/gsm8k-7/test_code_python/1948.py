def solution():
    small_price = 1
    medium_price = 2
    large_price = 3

    total_sales = 50
    small_sales = 11
    medium_sales = 24

    # Calculate the total sales of large cups of lemonade
    large_sales = total_sales - small_sales - medium_sales

    # Calculate the number of large cups of lemonade sold
    num_large_cups = large_sales / large_price
    result = num_large_cups
    return result

print(solution())