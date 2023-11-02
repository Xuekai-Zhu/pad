def solution():
    num_large_posters_per_day = 2
    large_poster_selling_price = 10
    large_poster_production_cost = 5

    num_small_posters_per_day = 5 - num_large_posters_per_day
    small_poster_selling_price = 6
    small_poster_production_cost = 3

    num_days = 5

    # Calculate the total revenue from selling all posters
    total_revenue = (num_large_posters_per_day * large_poster_selling_price +
                     num_small_posters_per_day * small_poster_selling_price) * num_days

    # Calculate the total cost of producing all posters
    total_cost = (num_large_posters_per_day * large_poster_production_cost +
                  num_small_posters_per_day * small_poster_production_cost) * num_days

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())