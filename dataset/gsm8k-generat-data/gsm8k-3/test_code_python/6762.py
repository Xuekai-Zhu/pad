def solution():
    """A third of all the cats in the village have spots. A quarter of the spotted cats in the village are fluffy. If there are 120 cats in the village, how many of the cats are spotted and fluffy?"""
    # Calculate the number of spotted cats in the village
    spotted_cats = 120 / 3

    # Calculate the number of fluffy spotted cats
    fluffy_spotted_cats = spotted_cats / 4

    # Display the number of spotted and fluffy cats
    result = fluffy_spotted_cats
    return result

print(solution())