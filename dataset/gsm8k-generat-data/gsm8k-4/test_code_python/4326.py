def solution():
    """Liam and Claire picked and sold oranges to save for their mother's birthday gift. Liam picked 40 oranges and sold them at $2.50 for 2 while Claire picked 30 oranges and sold them at $1.20 each. If all of their oranges were sold, how much are they going to save for their mother's birthday gift?"""
    # Define Liam's sales
    liam_oranges = 40
    liam_price = 2.5
    liam_sale = liam_oranges // 2 * liam_price

    # Define Claire's sales
    claire_oranges = 30
    claire_price = 1.2
    claire_sale = claire_oranges * claire_price

    # Calculate the total sales
    total_sales = liam_sale + claire_sale

    # return the result
    result = total_sales
    return result

print(solution())