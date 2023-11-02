def solution():
    """Shelly and Sam love to go deep sea fishing for swordfish.  Each time they go deep sea fishing,
    Shelly catches 2 less than five swordfish, and Sam catches one less swordfish than Shelly.
    If Sam and Shelly go fishing 5 times, how many swordfish do they catch in total?"""
    # Define the number of swordfish caught by Shelly
    shelly_swordfish = []

    # Define the number of swordfish caught by Sam
    sam_swordfish = []

    # Calculate the number of swordfish caught by Shelly and Sam for each fishing trip
    for i in range(5):
        shelly_swordfish.append(5 - 2 * i)
        sam_swordfish.append(shelly_swordfish[i] - 1)

    # Calculate the total number of swordfish caught by Shelly and Sam
    total_swordfish = sum(shelly_swordfish) + sum(sam_swordfish)

    # Display the total number of swordfish caught
    result = total_swordfish
    return result

print(solution())