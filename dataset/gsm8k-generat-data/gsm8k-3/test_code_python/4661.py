def solution():
    """To upgrade her kitchen, Amanda is changing out the doorknobs/pulls.  She’s replacing 18 cabinet knobs, which cost $2.50 each and 8 drawer pulls which cost $4.00.  How much will the kitchen upgrade cost her?"""
    # Define the cost of each type of hardware
    CABINET_KNOB_COST = 2.5
    DRAWER_PULL_COST = 4.0

    # Define the number of each type of hardware Amanda is purchasing
    num_cabinet_knobs = 18
    num_drawer_pulls = 8

    # Calculate the total cost of the cabinet knobs
    cabinet_knob_cost = num_cabinet_knobs * CABINET_KNOB_COST

    # Calculate the total cost of the drawer pulls
    drawer_pull_cost = num_drawer_pulls * DRAWER_PULL_COST

    # Calculate the total cost of the kitchen upgrade
    total_cost = cabinet_knob_cost + drawer_pull_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())