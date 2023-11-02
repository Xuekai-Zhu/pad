def solution():
    """Clyde and Grace are building block towers. Grace’s tower is 8 times the size of Clyde’s at 40 inches tall. How many inches taller is Grace’s tower than Clyde’s?"""
    # Define the initial height of Clyde's tower
    clyde_height = 0

    # Define the height of Grace's tower in inches
    grace_height = 40

    # Calculate the height of Clyde's tower as a fraction of Grace's
    clyde_fraction = 1/8

    # Calculate the height of Clyde's tower in inches
    clyde_height = grace_height * clyde_fraction

    # Calculate the difference in height between the two towers
    height_difference = grace_height - clyde_height

    # return the result
    result = height_difference
    return result

print(solution())