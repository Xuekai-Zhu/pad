def solution():
    """Wes wants to place a large planter pot at each corner of his rectangle-shaped pool. Each planter will have a large palm fern that is $15.00 per plant, 4 creeping jennies that costs $4.00 per plant and 4 geraniums that cost $3.50 per plant. How much will it cost to fill all the pots?"""
    num_pots = 4
    cost_palm_fern = 15.00
    cost_creeping_jenny = 4.00
    cost_geranium = 3.50
    num_plants_per_pot = 1 + 4 + 4 # 1 palm fern, 4 creeping jennies, 4 geraniums
    cost_per_pot = cost_palm_fern + (4 * cost_creeping_jenny) + (4 * cost_geranium) 
    total_cost = num_pots * cost_per_pot
    result = total_cost
    return result

print(solution())