def solution():
    
    forest_trolls = 6
    bridge_trolls = (forest_trolls * 4) - 6
    plains_trolls = bridge_trolls / 2
    total_trolls = forest_trolls + bridge_trolls + plains_trolls
    result = total_trolls
    return result

print(solution())