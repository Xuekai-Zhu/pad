def solution():
    # Lisa visited 6 rehabilitation centers
    lisa_centers = 6

    # Jude visited half fewer rehabilitation centers as Lisa did
    jude_centers = lisa_centers / 2

    # Han visited 2 less than twice as many rehabilitation centers as Jude did
    han_centers = 2 * jude_centers - 2

    # Jane visited 6 more than twice as many rehabilitation centers as Han
    jane_centers = 2 * han_centers + 6

    # Total number of rehabilitation centers visited
    total_centers = lisa_centers + jude_centers + han_centers + jane_centers

    result = total_centers
    return result

print(solution())