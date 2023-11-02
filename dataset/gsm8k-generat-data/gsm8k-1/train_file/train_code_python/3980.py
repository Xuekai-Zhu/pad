def solution():
    """James visits 20 houses to try and make a sale. He manages to sell something in every house. The next day he visits twice as many houses but only sold to 80% of houses. If he sold two things at each house in each of the two days, how many items did he sell?"""
    initial_houses_visited = 20
    initial_sales = initial_houses_visited
    next_day_houses_visited = initial_houses_visited * 2
    next_day_sales = int(next_day_houses_visited * 0.8)
    total_sales = (initial_sales + next_day_sales) * 2
    result = total_sales
    return result

print(solution())