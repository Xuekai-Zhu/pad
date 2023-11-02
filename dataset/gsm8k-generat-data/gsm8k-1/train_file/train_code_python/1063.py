def solution():
    """Harry owns 3 geckos, 2 iguanas, and 4 snakes. If he spends $10 to feed each snake, $5 to feed each iguana, and $15 to feed each gecko every month, how much does he spend every year to feed all his pets?"""
    geckos = 3
    iguanas = 2
    snakes = 4
    gecko_monthly_cost = 15
    iguana_monthly_cost = 5
    snake_monthly_cost = 10
    total_monthly_cost = (geckos * gecko_monthly_cost) + (iguanas * iguana_monthly_cost) + (snakes * snake_monthly_cost)
    yearly_cost = total_monthly_cost * 12
    result = yearly_cost
    return result

print(solution())