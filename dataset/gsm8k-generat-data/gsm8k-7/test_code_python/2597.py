def solution():
    lisa_centers = 6

    # Calculate how many rehabilitation centers Jude visited
    jude_centers = (lisa_centers / 2) - 0.5

    # Calculate how many rehabilitation centers Han visited
    han_centers = (2 * jude_centers) - 2

    # Calculate how many rehabilitation centers Jane visited
    jane_centers = (2 * han_centers) + 6

    # Calculate the total number of rehabilitation centers visited
    total_centers = lisa_centers + jude_centers + han_centers + jane_centers
    result = total_centers
    return result

print(solution())