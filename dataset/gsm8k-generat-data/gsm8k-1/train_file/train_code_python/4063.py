def solution():
    """The novelty shop on the Starship Conundrum sells magazines and chocolates. The cost of four chocolate bars is equal to the cost of 8 magazines. If one magazine costs $1, how much does a dozen chocolate bars cost, in dollars?"""
    cost_of_4_chocolate_bars = 8
    cost_of_1_chocolate_bar = cost_of_4_chocolate_bars / 4
    cost_of_12_chocolate_bars = cost_of_1_chocolate_bar * 12
    result = cost_of_12_chocolate_bars
    return result

print(solution())