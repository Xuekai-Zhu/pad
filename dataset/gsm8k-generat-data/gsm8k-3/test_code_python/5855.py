def solution():
    """Four days ago, Carlos bought a bag of gummy worms. Every day he ate half of the remaining gummy worms. After eating half of the remainder on the fourth day, he now has 4 gummy worms left. How many gummy worms were in the bag when Carlos bought it?"""
    # Start with the number of gummy worms Carlos has left
    gummy_worms = 4

    # On the third day, Carlos had twice as many gummy worms as he has now
    gummy_worms *= 2

    # On the second day, Carlos had twice as many gummy worms as he had on the third day
    gummy_worms *= 2

    # On the first day, Carlos had twice as many gummy worms as he had on the second day
    gummy_worms *= 2

    # Display the original number of gummy worms
    result = gummy_worms
    return result

print(solution())