def solution():
    """Hannah is at a restaurant. She spends $23 in total on an entree and a dessert. If the entree costs $5 more than the dessert, how much does the entree cost, in dollars?"""
    total_cost = 23
    dessert_cost = (total_cost - 5) / 2
    entree_cost = dessert_cost + 5
    result = entree_cost
    return result

print(solution())