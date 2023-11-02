def solution():
    """Laura needs to buy window treatments for 3 windows in her house. She will need to buy a set of sheers and a set of drapes for each window. The sheers cost $40.00 a pair and the drapes cost $60.00 a pair. How much will the window treatments cost?"""
    num_windows = 3
    cost_sheers = 40
    cost_drapes = 60
    total_cost = (cost_sheers + cost_drapes) * 2 * num_windows
    result = total_cost
    return result

print(solution())