def solution():
    """Michael makes birdhouses to sell at craft shows. He charges $22 for each large birdhouse, $16 for each medium birdhouse, and $7 for each small birdhouse. This week, he sold 2 large birdhouses, 2 medium birdhouses, and 3 small birdhouses. How much money, in dollars, did he make this week?"""
    # Define the prices for each type of birdhouse
    large_price = 22
    medium_price = 16
    small_price = 7

    # Define the number of each type of birdhouse sold
    num_large = 2
    num_medium = 2
    num_small = 3

    # Calculate the total sales for each type of birdhouse
    large_sales = num_large * large_price
    medium_sales = num_medium * medium_price
    small_sales = num_small * small_price

    # Calculate the total sales for all birdhouses
    total_sales = large_sales + medium_sales + small_sales

    # Return the result
    result = total_sales
    return result

print(solution())