def solution():
    """Four days ago, Carlos bought a bag of gummy worms. Every day he ate half of the remaining gummy worms. After eating half of the remainder on the fourth day, he now has 4 gummy worms left. How many gummy worms were in the bag when Carlos bought it?"""
    remaining_worms = 4
    days = 4
    while days > 0:
        remaining_worms = remaining_worms * 2
        days -= 1
    initial_worms = remaining_worms
    result = initial_worms
    return result

print(solution())