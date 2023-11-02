def solution():
    """A developer was buying land. He bought 4 acres at $1,863 per acre. He then split the land he purchased into 9 lots. How much should he sell each lot for just to break even?"""
    total_cost = 4 * 1863
    cost_per_lot = total_cost / 9
    result = cost_per_lot
    return result

print(solution())