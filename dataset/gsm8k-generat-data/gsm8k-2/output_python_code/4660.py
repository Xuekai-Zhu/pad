def solution():
    """To upgrade her kitchen, Amanda is changing out the doorknobs/pulls. She’s replacing 18 cabinet knobs, which cost $2.50 each and 8 drawer pulls which cost $4.00. How much will the kitchen upgrade cost her?"""
    cabinet_knob_price = 2.5
    drawer_pull_price = 4
    cabinet_knob_count = 18
    drawer_pull_count = 8
    total_cost = (cabinet_knob_price * cabinet_knob_count) + (drawer_pull_price * drawer_pull_count)
    result = total_cost
    return result

print(solution())