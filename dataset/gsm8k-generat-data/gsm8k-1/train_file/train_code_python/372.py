def solution():
    """Alison bought some storage tubs for her garage. She bought 3 large ones and 6 small ones, for $48 total. If the large tubs cost $6, how much do the small ones cost?"""
    total_tubs = 9
    cost_of_large_tubs = 6
    total_cost = 48
    cost_of_small_tubs = (total_cost - (cost_of_large_tubs * 3)) / 6
    result = cost_of_small_tubs
    return result

print(solution())