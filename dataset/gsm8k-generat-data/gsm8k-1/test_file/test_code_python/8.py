def solution():
    """Carlos is planting a lemon tree. The tree will cost $90 to plant. Each year it will grow 7 lemons, which he can sell for $1.5 each. It costs $3 a year to water and feed the tree. How many years will it take before he starts earning money on the lemon tree?"""
    tree_cost = 90
    lemon_price = 1.5
    yearly_cost = 3
    lemons_per_year = 7
    years = 0
    while lemons_per_year * lemon_price - yearly_cost <= 0:
        years += 1
        lemons_per_year += 7
    result = years
    return result

print(solution())