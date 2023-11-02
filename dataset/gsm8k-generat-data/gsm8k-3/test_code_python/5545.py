def solution():
    """Wes wants to place a large planter pot at each corner of his rectangle-shaped pool.  Each planter will have a large palm fern that is $15.00 per plant, 4 creeping jennies that costs $4.00 per plant and 4 geraniums that cost $3.50 per plant.  How much will it cost to fill all the pots?"""
    # Define the cost of each type of plant
    PALM_FERN_COST = 15
    CREEPING_JENNY_COST = 4
    GERANIUM_COST = 3.5

    # Define the number of plants needed for each pot
    PALM_FERN_COUNT = 1
    CREEPING_JENNY_COUNT = 4
    GERANIUM_COUNT = 4

    # Define the number of pots needed
    POT_COUNT = 4

    # Calculate the total cost of the plants for each pot
    pot_cost = (PALM_FERN_COST * PALM_FERN_COUNT) + (CREEPING_JENNY_COST * CREEPING_JENNY_COUNT) + (GERANIUM_COST * GERANIUM_COUNT)

    # Calculate the total cost of all the pots
    total_cost = POT_COUNT * pot_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())