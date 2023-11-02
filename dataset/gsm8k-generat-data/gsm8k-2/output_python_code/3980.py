def solution():
    """James visits 20 houses to try and make a sale. He manages to sell something in every house. The next day he visits twice as many houses but only sold to 80% of houses. If he sold two things at each house in each of the two days, how many items did he sell?"""
    first_day_sales = 20 * 2
    second_day_sales = 40 * 0.8 * 2
    total_sales = first_day_sales + second_day_sales
    result = total_sales
    return result

print(solution())