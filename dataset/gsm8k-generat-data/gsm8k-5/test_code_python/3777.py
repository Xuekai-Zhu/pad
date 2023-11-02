def solution():
    # Number of siblings Masud has
    masud_siblings = 60

    # Number of siblings Carlos has
    carlos_siblings = 3/4 * masud_siblings

    # Number of siblings Janet has
    janet_siblings = 4 * masud_siblings - 60

    # Difference between the number of siblings Janet and Carlos have
    difference = janet_siblings - carlos_siblings

    result = difference
    return result

print(solution())