def solution():
    """The kids in Ms. Swanson's class have an average of 5 zits each. The kids in Mr. Jones' class have an average of six zits each. If there are 25 kids in Ms. Swanson's class and 32 in Mr. Jones' class, how many more zits are there in Mr. Jones' class than in Ms. Swanson's?"""
    # Calculate the total number of zits in Ms. Swanson's class
    swanson_zits = 25 * 5

    # Calculate the total number of zits in Mr. Jones' class
    jones_zits = 32 * 6

    # Calculate the difference in the total number of zits
    zit_difference = jones_zits - swanson_zits

    # Display the difference in the total number of zits
    result = zit_difference
    return result

print(solution())