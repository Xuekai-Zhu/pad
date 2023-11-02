def solution():
    """Laran has started a poster business. She is selling 5 posters per day at school. Two posters per day are her large posters that sell for $10. The large posters cost her $5 to make. The remaining posters are small posters that sell for $6. They cost $3 to produce. How much profit, in dollars, does Laran make per 5-day school week?"""
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