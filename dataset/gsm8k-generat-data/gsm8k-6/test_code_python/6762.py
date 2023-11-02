def solution():
    # Calculate the number of spotted cats in the village
    spotted_cats = 120 / 3  # a third of all cats in the village have spots

    # Calculate the number of spotted cats that are fluffy
    spotted_fluffy_cats = (1 / 4) * spotted_cats  # a quarter of the spotted cats are fluffy

    result = spotted_fluffy_cats
    return result

print(solution())