def solution():
    # Find the number of siblings Janet has
    masud_siblings = 60
    janet_siblings = 4*masud_siblings - 60

    # Find the number of siblings Carlos has
    carlos_siblings = (3/4)*masud_siblings

    # Find the difference in the number of siblings Janet and Carlos have
    difference = janet_siblings - carlos_siblings
    result = difference
    return result

print(solution())