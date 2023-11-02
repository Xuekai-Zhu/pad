def solution():
    """Laura needs to buy window treatments for 3 windows in her house. She will need to buy a set of sheers and a set of drapes for each window. The sheers cost $40.00 a pair and the drapes cost $60.00 a pair. How much will the window treatments cost?"""
    windows = 3
    sheers_cost = 40
    drapes_cost = 60
    total_cost = (sheers_cost + drapes_cost) * windows
    result = total_cost
    return result

print(solution())