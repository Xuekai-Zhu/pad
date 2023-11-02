def solution():
    """A third of all the cats in the village have spots. A quarter of the spotted cats in the village are fluffy. If there are 120 cats in the village, how many of the cats are spotted and fluffy?"""
    total_cats = 120
    spotted_cats = total_cats / 3
    fluffy_spotted_cats = spotted_cats / 4
    result = fluffy_spotted_cats
    return result

print(solution())