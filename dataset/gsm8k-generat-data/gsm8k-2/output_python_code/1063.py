def solution():
    """Harry owns 3 geckos, 2 iguanas, and 4 snakes. If he spends $10 to feed each snake, $5 to feed each iguana, and $15 to feed each gecko every month, how much does he spend every year to feed all his pets?"""
    gecko_cost = 15 * 12
    iguana_cost = 5 * 12
    snake_cost = 10 * 4 * 12
    total_cost = (3 * gecko_cost) + (2 * iguana_cost) + snake_cost
    result = total_cost
    return result

print(solution())