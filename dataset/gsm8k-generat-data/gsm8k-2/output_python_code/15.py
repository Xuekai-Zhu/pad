def solution():
    """James creates a media empire. He creates a movie for $2000. Each DVD cost $6 to make. He sells it for 2.5 times that much. He sells 500 movies a day for 5 days a week. How much profit does he make in 20 weeks?"""
    movie_cost = 2000
    dvd_cost = 6
    dvd_price = 2.5 * dvd_cost
    daily_profit = (500 * dvd_price) - (500 * dvd_cost) - (movie_cost/5)
    weekly_profit = daily_profit * 5
    total_profit = weekly_profit * 20
    result = total_profit
    return result

print(solution())