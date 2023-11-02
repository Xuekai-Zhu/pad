def solution():
    # Calculate the total cost of feeding Harry's pets for 1 month
    gecko_cost = 15 * 3  # Harry owns 3 geckos and spends $15 to feed each gecko
    iguana_cost = 5 * 2  # Harry owns 2 iguanas and spends $5 to feed each iguana
    snake_cost = 10 * 4  # Harry owns 4 snakes and spends $10 to feed each snake
    monthly_cost = gecko_cost + iguana_cost + snake_cost

    # Calculate the total cost of feeding Harry's pets for 1 year
    yearly_cost = monthly_cost * 12
    result = yearly_cost
    return result

print(solution())