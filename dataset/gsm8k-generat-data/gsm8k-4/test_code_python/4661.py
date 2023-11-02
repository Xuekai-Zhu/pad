def solution():
    """To upgrade her kitchen, Amanda is changing out the doorknobs/pulls. She’s replacing 18 cabinet knobs, which cost $2.50 each and 8 drawer pulls which cost $4.00. How much will the kitchen upgrade cost her?"""
    # Define the cost of a cabinet knob and a drawer pull
    CABINET_KNOB_COST = 2.5
    DRAWER_PULL_COST = 4.0

    # Calculate the total cost of the cabinet knobs and drawer pulls
    total_cost = (CABINET_KNOB_COST * 18) + (DRAWER_PULL_COST * 8)

    result = total_cost
    return result

print(solution())