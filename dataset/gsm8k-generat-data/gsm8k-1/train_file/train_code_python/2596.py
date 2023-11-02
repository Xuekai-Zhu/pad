def solution():
    """When Jane visited Iran, she visited 6 more than twice as many rehabilitation centers as Han. Han visited 2 less than twice as many rehabilitation centers as Jude did. Jude visited half fewer rehabilitation centers as Lisa did. If Lisa visited 6 rehabilitation centers, how many rehabilitation centers did they all visit assuming they are all different?"""
    lisa_centers = 6
    jude_centers = lisa_centers / 2
    han_centers = (2 * jude_centers) - 2
    jane_centers = (2 * han_centers) + 6
    total_centers = lisa_centers + jude_centers + han_centers + jane_centers
    result = total_centers
    return result

print(solution())