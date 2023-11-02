def solution():
    """During the Mardi Gras parade, Latch caught four less than three times as many necklaces as did Rhonda.  If Rhonda caught half as many necklaces as did Boudreaux, and Boudreaux caught twelve necklaces, how many necklaces did Latch catch?"""
    # Define the number of necklaces caught by Boudreaux
    boudreaux_necklaces = 12

    # Calculate the number of necklaces caught by Rhonda
    rhonda_necklaces = boudreaux_necklaces / 2

    # Calculate the number of necklaces caught by Latch
    latch_necklaces = 3 * rhonda_necklaces - 4

    # Return the result
    result = latch_necklaces
    return result

print(solution())