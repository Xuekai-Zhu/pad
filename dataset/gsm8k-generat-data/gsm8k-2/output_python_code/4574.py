def solution():
    """Laran has started a poster business. She is selling 5 posters per day at school. Two posters per day are her large posters that sell for $10. The large posters cost her $5 to make. The remaining posters are small posters that sell for $6. They cost $3 to produce. How much profit, in dollars, does Laran make per 5-day school week?"""
    total_days = 5
    large_posters = 2
    small_posters = 5 - large_posters
    large_poster_price = 10
    small_poster_price = 6
    large_poster_cost = 5
    small_poster_cost = 3
    total_sales = (large_posters * large_poster_price + small_posters * small_poster_price) * total_days
    total_cost = (large_posters * large_poster_cost + small_posters * small_poster_cost) * total_days
    total_profit = total_sales - total_cost
    result = total_profit
    return result

print(solution())