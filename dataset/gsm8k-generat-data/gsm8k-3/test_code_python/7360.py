def solution():
    """Apollo pulls the sun across the sky every night. Once a month, his fiery chariot’s wheels need to be replaced. He trades golden apples to Hephaestus the blacksmith to get Hephaestus to make him new wheels. Hephaestus raised his rates halfway through the year and now demands twice as many golden apples as before. He charged three golden apples for the first six months. How many golden apples does Apollo have to pay for the entire year of chariot wheels?"""
    # Define the cost per month for the first six months
    COST_1 = 3

    # Define the cost per month for the last six months
    COST_2 = COST_1 * 2

    # Calculate the total cost for the year
    total_cost = (COST_1 * 6) + (COST_2 * 6)

    # Display the total cost
    result = total_cost
    return result

print(solution())