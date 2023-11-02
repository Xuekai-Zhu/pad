def solution():
    """During the Mardi Gras parade, Latch caught four less than three times as many necklaces as did Rhonda. If Rhonda caught half as many necklaces as did Boudreaux, and Boudreaux caught twelve necklaces, how many necklaces did Latch catch?"""
    boudreaux_necklaces = 12
    rhonda_necklaces = boudreaux_necklaces / 2
    latch_necklaces = 3 * rhonda_necklaces - 4
    result = latch_necklaces
    return result

print(solution())