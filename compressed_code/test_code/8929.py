def solution():
    
    initial_houses_visited = 20
    initial_sales = initial_houses_visited
    next_day_houses_visited = initial_houses_visited * 2
    next_day_sales = int(next_day_houses_visited * 0.8)
    total_sales = (initial_sales + next_day_sales) * 2
    result = total_sales
    return result

print(solution())