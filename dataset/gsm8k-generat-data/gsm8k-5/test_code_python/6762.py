def solution():
    total_cats = 120  # There are 120 cats in the village

    # Calculate the number of cats with spots
    cats_with_spots = total_cats // 3

    # Calculate the number of spotted cats that are fluffy
    spotted_fluffy_cats = (cats_with_spots // 4)

    result = spotted_fluffy_cats
    return result

print(solution())