def solution():
    """Wes wants to place a large planter pot at each corner of his rectangle-shaped pool. Each planter will have a large palm fern that is $15.00 per plant, 4 creeping jennies that costs $4.00 per plant and 4 geraniums that cost $3.50 per plant. How much will it cost to fill all the pots?"""
    # Define the number of plants needed for each pot
    ferns_per_pot = 1
    jennies_per_pot = 4
    geraniums_per_pot = 4

    # Define the cost of each type of plant
    fern_cost = 15.00
    jenny_cost = 4.00
    geranium_cost = 3.50

    # Define the number of pots
    num_pots = 4

    # Calculate the total cost of all the plants
    total_cost = (ferns_per_pot * fern_cost + jennies_per_pot * jenny_cost + geraniums_per_pot * geranium_cost) * num_pots

    # return the result
    result = total_cost
    return result

print(solution())