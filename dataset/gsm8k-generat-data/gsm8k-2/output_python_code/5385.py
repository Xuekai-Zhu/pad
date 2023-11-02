def solution():
    """Erin counts six trolls hiding by the path in the forest, 6 less than four times that number of trolls hiding under the bridge, and half as many trolls hiding in the plains as under the bridge. How many trolls did she count in total?"""
    trolls_forest = 6
    trolls_bridge = (trolls_forest + 6) / 4
    trolls_plains = trolls_bridge / 2
    total_trolls = trolls_forest + trolls_bridge + trolls_plains
    result = total_trolls
    return result

print(solution())