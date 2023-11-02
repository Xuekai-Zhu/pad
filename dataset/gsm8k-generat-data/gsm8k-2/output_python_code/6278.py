def solution():
    """Michael makes birdhouses to sell at craft shows. He charges $22 for each large birdhouse, $16 for each medium birdhouse, and $7 for each small birdhouse. This week, he sold 2 large birdhouses, 2 medium birdhouses, and 3 small birdhouses. How much money, in dollars, did he make this week?"""
    large_price = 22
    medium_price = 16
    small_price = 7
    num_large = 2
    num_medium = 2
    num_small = 3
    total_money = (large_price * num_large) + (medium_price * num_medium) + (small_price * num_small)
    result = total_money
    return result

print(solution())