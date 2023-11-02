def solution():
    dogs = 4
    cats = 3

    # Each animal needs 2 legs covered, so Haleigh needs to buy twice as many leggings as there are animals
    pairs_of_leggings = (dogs + cats) * 2
    result = pairs_of_leggings
    return result

print(solution())