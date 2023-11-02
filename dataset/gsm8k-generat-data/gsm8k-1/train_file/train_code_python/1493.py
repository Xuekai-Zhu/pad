def solution():
    """Micah has 7 fish in his aquarium. Kenneth has three times as many fish in his aquarium and Matthias has 15 less fish than Kenneth in his aquarium. How many fish do the boys have in total?"""
    micah_fish = 7
    kenneth_fish = 3 * micah_fish
    matthias_fish = kenneth_fish - 15
    total_fish = micah_fish + kenneth_fish + matthias_fish
    result = total_fish
    return result

print(solution())