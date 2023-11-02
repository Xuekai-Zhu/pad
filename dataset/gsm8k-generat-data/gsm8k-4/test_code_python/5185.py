def solution():
    """Shelly and Sam love to go deep sea fishing for swordfish. Each time they go deep sea fishing, Shelly catches 2 less than five swordfish, and Sam catches one less swordfish than Shelly. If Sam and Shelly go fishing 5 times, how many swordfish do they catch in total?"""
    # Initialize the variables for the number of swordfish caught by each person
    shelly_swordfish = 0
    sam_swordfish = 0

    # Go deep sea fishing 5 times
    for i in range(5):
        # Calculate the number of swordfish caught by Shelly
        shelly_swordfish += 5 - 2

        # Calculate the number of swordfish caught by Sam
        sam_swordfish += 5 - 3

    # Calculate the total number of swordfish caught
    total_swordfish = shelly_swordfish + sam_swordfish

    result = total_swordfish
    return result

print(solution())