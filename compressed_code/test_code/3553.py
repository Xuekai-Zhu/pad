def solution():
    
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