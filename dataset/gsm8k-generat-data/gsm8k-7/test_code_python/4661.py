def solution():
    num_cabinet_knobs = 18
    cabinet_knob_cost = 2.5

    num_drawer_pulls = 8
    drawer_pull_cost = 4.0

    # Calculate the total cost of all cabinet knobs
    total_cabinet_knob_cost = num_cabinet_knobs * cabinet_knob_cost

    # Calculate the total cost of all drawer pulls
    total_drawer_pull_cost = num_drawer_pulls * drawer_pull_cost

    # Calculate the total cost of the kitchen upgrade
    total_cost = total_cabinet_knob_cost + total_drawer_pull_cost
    result = total_cost
    return result

print(solution())