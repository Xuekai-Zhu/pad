def solution():
    """Four days ago, Carlos bought a bag of gummy worms. Every day he ate half of the remaining gummy worms. After eating half of the remainder on the fourth day, he now has 4 gummy worms left. How many gummy worms were in the bag when Carlos bought it?"""
    remaining_worms = 4
    for i in range(4):
        remaining_worms *= 2
    total_worms = remaining_worms * 2
    result = total_worms
    return result

print(solution())