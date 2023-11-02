def solution():
    """Michael makes birdhouses to sell at craft shows. He charges $22 for each large birdhouse, $16 for each medium birdhouse, and $7 for each small birdhouse. This week, he sold 2 large birdhouses, 2 medium birdhouses, and 3 small birdhouses. How much money, in dollars, did he make this week?"""
    # Define the prices for each size of birdhouse
    LARGE_PRICE = 22
    MEDIUM_PRICE = 16
    SMALL_PRICE = 7

    # Define the number of each size of birdhouse sold
    num_large = 2
    num_medium = 2
    num_small = 3

    # Calculate the total revenue
    total_revenue = (num_large * LARGE_PRICE) + (num_medium * MEDIUM_PRICE) + (num_small * SMALL_PRICE)

    # Display the total revenue
    result = total_revenue
    return result

print(solution())