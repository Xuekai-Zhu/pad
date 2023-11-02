def solution():
    """Samantha, Aira, and Joe received 6 rubber bands each after they divided their bands equally. If Samantha had 5 more bands than Aira and Aira had 1 fewer band than Joe, how many rubber bands did Aira have?"""
    # Define the number of rubber bands received by each person
    bands_per_person = 6

    # Calculate the total number of rubber bands
    total_bands = bands_per_person * 3

    # Define the number of bands Aira has as x
    x = None

    # Calculate the number of bands Samantha has using the given information
    samantha_bands = x + 5

    # Calculate the number of bands Joe has using the given information
    joe_bands = x + 1

    # Calculate the total number of rubber bands using the equation: total_bands = samantha_bands + aira_bands + joe_bands
    aira_bands = (total_bands - samantha_bands - joe_bands) / 3

    # Return the number of rubber bands Aira has
    result = aira_bands
    return result

print(solution())