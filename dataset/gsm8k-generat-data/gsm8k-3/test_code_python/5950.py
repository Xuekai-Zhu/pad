def solution():
    """During the Mardi Gras parade, Latch caught four less than three times as many necklaces as did Rhonda.  If Rhonda caught half as many necklaces as did Boudreaux, and Boudreaux caught twelve necklaces, how many necklaces did Latch catch?"""
    # Calculate the number of necklaces caught by Boudreaux
    boudreaux = 12

    # Calculate the number of necklaces caught by Rhonda
    rhonda = boudreaux / 2

    # Calculate the number of necklaces caught by Latch
    latch = 3 * rhonda - 4

    # Display the number of necklaces caught by Latch
    result = latch
    return result

print(solution())