def solution():
    """The novelty shop on the Starship Conundrum sells magazines and chocolates. The cost of four chocolate bars is equal to the cost of 8 magazines. If one magazine costs $1, how much does a dozen chocolate bars cost, in dollars?"""
    cost_per_magazine = 1
    num_chocolates = 12
    num_magazines = num_chocolates * 2
    cost_per_chocolate = (4 * cost_per_magazine) / 8
    total_cost = num_chocolates * cost_per_chocolate
    result = total_cost
    return result

print(solution())