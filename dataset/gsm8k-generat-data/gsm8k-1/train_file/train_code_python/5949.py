def solution():
    """During the Mardi Gras parade, Latch caught four less than three times as many necklaces as did Rhonda. If Rhonda caught half as many necklaces as did Boudreaux, and Boudreaux caught twelve necklaces, how many necklaces did Latch catch?"""
    boudreaux_catches = 12
    rhonda_catches = boudreaux_catches / 2
    latch_catches = (3 * rhonda_catches) - 4
    result = latch_catches
    return result

print(solution())