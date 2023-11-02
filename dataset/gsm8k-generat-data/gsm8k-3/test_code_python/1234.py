def solution():
    """A bag of pistachios has 80 pistachios in it.  95 percent have shells, and 75 percent of those have shells that are opened.  How many pistachios in the bag have shells and have an opened shell?"""
    # Define the number of pistachios in the bag
    num_pistachios = 80

    # Calculate the number of pistachios with shells
    num_pistachios_with_shells = int(num_pistachios * 0.95)

    # Calculate the number of pistachios with shells that are opened
    num_pistachios_with_opened_shells = int(num_pistachios_with_shells * 0.75)

    # Display the number of pistachios with shells and opened shells
    result = num_pistachios_with_opened_shells
    return result

print(solution())