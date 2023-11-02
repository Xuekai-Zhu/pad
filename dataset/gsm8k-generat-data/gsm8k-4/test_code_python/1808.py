def solution():
    """The kids in Ms. Swanson's class have an average of 5 zits each. The kids in Mr. Jones' class have an average of six zits each. If there are 25 kids in Ms. Swanson's class and 32 in Mr. Jones' class, how many more zits are there in Mr. Jones' class than in Ms. Swanson's?"""
    # Define the number of kids in each class and the average number of zits per kid
    swanson_kids = 25
    jones_kids = 32
    swanson_zits = 5
    jones_zits = 6

    # Calculate the total number of zits in each class
    swanson_total_zits = swanson_kids * swanson_zits
    jones_total_zits = jones_kids * jones_zits

    # Calculate the difference in the total number of zits
    zit_difference = jones_total_zits - swanson_total_zits

    # Return the result
    result = zit_difference
    return result

print(solution())