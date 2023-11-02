def solution():
    """A bag of pistachios has 80 pistachios in it.  95 percent have shells, and 75 percent of those have shells that are opened.  How many pistachios in the bag have shells and have an opened shell?"""
    # Define the total number of pistachios in the bag
    total_pistachios = 80

    # Calculate the number of pistachios with shells
    pistachios_with_shells = total_pistachios * 0.95

    # Calculate the number of pistachios with shells that are opened
    pistachios_with_opened_shells = pistachios_with_shells * 0.75

    # return the result
    result = pistachios_with_opened_shells
    return result

print(solution())