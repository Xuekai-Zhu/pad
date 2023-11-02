def solution():
    """In a section of the forest, there are 100 weasels and 50 rabbits. Three foxes invade this region and hunt the rodents. Each fox catches an average of 4 weasels and 2 rabbits per week. How many rabbits and weasels will be left after 3 weeks?"""
    initial_weasels = 100
    initial_rabbits = 50
    foxes = 3
    weasels_caught = foxes * 4
    rabbits_caught = foxes * 2
    remaining_weeks = 3
    for i in range(remaining_weeks):
        initial_weasels -= weasels_caught
        initial_rabbits -= rabbits_caught

    result = (initial_weasels, initial_rabbits)
    return result

print(solution())