def solution():
    """A third of all the cats in the village have spots. A quarter of the spotted cats in the village are fluffy. If there are 120 cats in the village, how many of the cats are spotted and fluffy?"""
    # Calculate the number of cats that are spotted
    spotted_cats = 120 / 3

    # Calculate the number of spotted cats that are fluffy
    spotted_fluffy_cats = spotted_cats / 4

    # return the result
    result = spotted_fluffy_cats
    return result

print(solution())