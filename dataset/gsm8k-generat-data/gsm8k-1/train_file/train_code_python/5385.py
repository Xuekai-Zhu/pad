def solution():
    """Erin counts six trolls hiding by the path in the forest, 6 less than four times that number of trolls hiding under the bridge, and half as many trolls hiding in the plains as under the bridge. How many trolls did she count in total?"""
    forest_trolls = 6
    bridge_trolls = (forest_trolls * 4) - 6
    plains_trolls = bridge_trolls / 2
    total_trolls = forest_trolls + bridge_trolls + plains_trolls
    result = total_trolls
    return result

print(solution())