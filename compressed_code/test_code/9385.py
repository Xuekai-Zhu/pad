def solution():
    
    large_posters_sold_per_week = 2 * 5
    small_posters_sold_per_week = (5 - 2) * 5
    revenue_from_large_posters = large_posters_sold_per_week * 10
    revenue_from_small_posters = small_posters_sold_per_week * 6
    cost_of_large_posters = large_posters_sold_per_week * 5
    cost_of_small_posters = small_posters_sold_per_week * 3
    total_profit = revenue_from_large_posters + revenue_from_small_posters - cost_of_large_posters - cost_of_small_posters
    result = total_profit
    return result

print(solution())