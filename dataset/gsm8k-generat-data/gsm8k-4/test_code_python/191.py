def solution():
    """In a section of the forest, there are 100 weasels and 50 rabbits. Three foxes invade this region and hunt the rodents. Each fox catches an average of 4 weasels and 2 rabbits per week. How many rabbits and weasels will be left after 3 weeks?"""
    # Define the initial number of weasels and rabbits
    weasels = 100
    rabbits = 50

    # Define the number of foxes and the number of weeks
    foxes = 3
    weeks = 3

    # Calculate the total number of weasels and rabbits hunted by the foxes
    total_weasels_hunted = foxes * 4 * weeks
    total_rabbits_hunted = foxes * 2 * weeks

    # Calculate the new number of weasels and rabbits
    weasels_remaining = weasels - total_weasels_hunted
    rabbits_remaining = rabbits - total_rabbits_hunted

    # return the result
    result = (rabbits_remaining, weasels_remaining)
    return result

print(solution())