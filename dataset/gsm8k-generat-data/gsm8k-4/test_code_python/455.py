def solution():
    """An amoeba reproduces by fission, splitting itself into two separate amoebae. An amoeba reproduces every two days. How many days will it take one amoeba to divide into 16 amoebae?"""
    # Define the initial number of amoebae and the target number of amoebae
    initial_amoebae = 1
    target_amoebae = 16

    # Initialize the day counter
    days = 0

    # Keep splitting the amoeba until the target number is reached
    while initial_amoebae < target_amoebae:
        initial_amoebae *= 2
        days += 2
        
    # Return the number of days it took to reach the target number
    result = days
    return result

print(solution())