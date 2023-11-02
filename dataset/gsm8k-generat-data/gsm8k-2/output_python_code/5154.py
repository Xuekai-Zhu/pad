def solution():
    """There are 6 forks in the cutlery drawer. There are 9 more knives than forks, and there are twice as many spoons as knives and half as many teaspoons as forks. After 2 of each cutlery is added to the drawer, how many pieces of cutlery are there in all?"""
    forks = 6
    knives = forks + 9
    spoons = 2 * knives
    teaspoons = forks / 2
    total_cutlery = forks + knives + spoons + teaspoons
    total_cutlery += 2 * 4 # adding 2 of each cutlery
    result = total_cutlery
    return result

print(solution())