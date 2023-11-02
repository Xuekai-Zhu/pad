def solution():
    """An amoeba reproduces by fission, splitting itself into two separate amoebae. An amoeba reproduces every two days. How many days will it take one amoeba to divide into 16 amoebae?"""
    # Define the starting number of amoebae and the desired number
    starting_amoebae = 1
    desired_amoebae = 16

    # Initialize the number of days
    days = 0

    # Loop until the desired number of amoebae is reached
    while starting_amoebae < desired_amoebae:
        starting_amoebae *= 2
        days += 2

    # Display the number of days
    result = days
    return result

print(solution())