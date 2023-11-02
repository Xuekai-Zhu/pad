def solution():
    # Given information
    masud_siblings = 60
    janet_siblings = 4*masud_siblings - 60
    carlos_siblings = 3/4 * masud_siblings

    # Difference between Janet and Carlos' siblings
    diff = janet_siblings - carlos_siblings

    # Return the result
    result = diff
    return result

print(solution())