def solution():
    """James buys 2 pairs of shoes a month. He spends $2640 on shoes each year. How much does he pay on average for each pair of shoes?"""
    pairs_per_month = 2
    cost_per_year = 2640
    months_per_year = 12
    total_pairs = pairs_per_month * months_per_year
    cost_per_pair = cost_per_year / total_pairs
    result = cost_per_pair
    return result

print(solution())