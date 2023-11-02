def solution():
    """In a section of the forest, there are 100 weasels and 50 rabbits. Three foxes invade this region and hunt the rodents. Each fox catches an average of 4 weasels and 2 rabbits per week. How many rabbits and weasels will be left after 3 weeks?"""
    initial_weasels = 100
    initial_rabbits = 50
    foxes = 3
    weasels_caught = foxes * 4
    rabbits_caught = foxes * 2
    total_weasels_caught = weasels_caught * 3
    total_rabbits_caught = rabbits_caught * 3
    final_weasels = initial_weasels - total_weasels_caught
    final_rabbits = initial_rabbits - total_rabbits_caught
    result = (final_weasels, final_rabbits)
    return result

print(solution())