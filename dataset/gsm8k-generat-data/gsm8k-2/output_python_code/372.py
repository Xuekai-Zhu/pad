def solution():
    """Alison bought some storage tubs for her garage. She bought 3 large ones and 6 small ones, for $48 total. If the large tubs cost $6, how much do the small ones cost?"""
    total_tubs = 9
    total_cost = 48
    large_tub_cost = 6
    large_tub_count = 3
    total_large_tub_cost = large_tub_count * large_tub_cost
    small_tub_cost = (total_cost - total_large_tub_cost) / (total_tubs - large_tub_count)
    result = small_tub_cost
    return result

print(solution())