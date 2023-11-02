def solution():
    
    movie_cost = 2000
    dvd_cost = 6
    sale_price = dvd_cost * 2.5
    daily_profit = (sale_price - dvd_cost) * 500
    weekly_profit = daily_profit * 5
    twenty_weeks_profit = weekly_profit * 20
    total_profit = twenty_weeks_profit - movie_cost
    result = total_profit
    return result

print(solution())