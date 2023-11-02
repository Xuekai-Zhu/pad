def solution():
    """Jeff orders a Halloween costume. He has to put in a 10% deposit and then pay the rest when he picks it up. The costume is 40% more expensive than last year's costume, which cost $250. How much did he pay when picking it up, in dollars?"""
    last_year_cost = 250
    deposit = 0.1 * (last_year_cost * 1.4)
    remaining_cost = (last_year_cost * 1.4) - deposit
    result = remaining_cost
    return result

print(solution())