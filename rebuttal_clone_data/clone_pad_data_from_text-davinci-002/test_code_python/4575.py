def solution():
    posters_sold_per_day = 5
    posters_sold_large = 2
    posters_sold_small = posters_sold_per_day - posters_sold_large
    cost_large_poster = 5
    cost_small_poster = 3
    price_large_poster = 10
    price_small_poster = 6

    total_cost = (cost_large_poster * posters_sold_large) + (cost_small_poster * posters_sold_small)
    total_revenue = (price_large_poster * posters_sold_large) + (price_small_poster * posters_sold_small)

    profit = total_revenue - total_cost
    return profit

print(solution())