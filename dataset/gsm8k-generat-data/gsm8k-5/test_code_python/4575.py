def solution():
    large_posters_sold_per_week = 2 * 5  # Laran sells 2 large posters per day for 5 school days
    small_posters_sold_per_week = (5 - 2) * 5  # Laran sells the remaining 3 small posters per day for 5 school days
    revenue_large_posters = large_posters_sold_per_week * 10  # Laran earns $10 for each large poster sold
    revenue_small_posters = small_posters_sold_per_week * 6  # Laran earns $6 for each small poster sold

    # Calculate the cost of producing the posters
    cost_large_posters = large_posters_sold_per_week * 5  # Laran spends $5 to make each large poster
    cost_small_posters = small_posters_sold_per_week * 3  # Laran spends $3 to make each small poster
    total_cost = cost_large_posters + cost_small_posters

    # Calculate the profit for the week
    profit = revenue_large_posters + revenue_small_posters - total_cost
    result = profit
    return result

print(solution())