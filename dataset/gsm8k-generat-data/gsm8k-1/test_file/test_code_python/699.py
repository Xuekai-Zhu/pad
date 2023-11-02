def solution():
    """Larry cooked dumplings for a group of friends. There are 8 males, including Larry, and 6 females among them. Each male ate 1 more dumpling than each female. How many dumplings did Larry cook if each female ate 3 dumplings and there were no leftovers?"""
    males = 8
    females = 6
    male_dumplings = females + 1
    female_dumplings = 3
    total_dumplings = males * male_dumplings + females * female_dumplings
    result = total_dumplings
    return result

print(solution())