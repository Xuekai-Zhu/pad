def solution():
    """Apollo pulls the sun across the sky every night. Once a month, his fiery chariot’s wheels need to be replaced. He trades golden apples to Hephaestus the blacksmith to get Hephaestus to make him new wheels. Hephaestus raised his rates halfway through the year and now demands twice as many golden apples as before. He charged three golden apples for the first six months. How many golden apples does Apollo have to pay for the entire year of chariot wheels?"""
    # Define the initial cost per wheel and the number of wheels per year
    INITIAL_COST = 3
    WHEELS_PER_YEAR = 12

    # Define the cost for the first six months and the cost for the second six months
    FIRST_SIX_MONTHS_COST = INITIAL_COST
    SECOND_SIX_MONTHS_COST = INITIAL_COST * 2

    # Calculate the total cost for the year
    total_cost = (FIRST_SIX_MONTHS_COST * 6) + (SECOND_SIX_MONTHS_COST * 6)

    # Return the result
    result = total_cost
    return result

print(solution())