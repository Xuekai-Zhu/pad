def solution():
    """Michael makes birdhouses to sell at craft shows. He charges $22 for each large birdhouse, $16 for each medium birdhouse, and $7 for each small birdhouse. This week, he sold 2 large birdhouses, 2 medium birdhouses, and 3 small birdhouses. How much money, in dollars, did he make this week?"""
    large_birdhouse_price = 22
    medium_birdhouse_price = 16
    small_birdhouse_price = 7
    num_large_birdhouses_sold = 2
    num_medium_birdhouses_sold = 2
    num_small_birdhouses_sold = 3
    total_money = (large_birdhouse_price * num_large_birdhouses_sold) + (medium_birdhouse_price * num_medium_birdhouses_sold) + (small_birdhouse_price * num_small_birdhouses_sold)
    result = total_money
    return result

print(solution())