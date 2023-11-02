def solution():
    """Wes wants to place a large planter pot at each corner of his rectangle-shaped pool. Each planter will have a large palm fern that is $15.00 per plant, 4 creeping jennies that costs $4.00 per plant and 4 geraniums that cost $3.50 per plant. How much will it cost to fill all the pots?"""
    
    # calculate the cost of each pot
    palm_fern_cost = 15
    creeping_jenny_cost = 4 * 4
    geranium_cost = 4 * 3.5
    pot_cost = palm_fern_cost + creeping_jenny_cost + geranium_cost
    
    # calculate the total cost for four pots
    total_cost = pot_cost * 4
    
    result = total_cost
    return result

print(solution())