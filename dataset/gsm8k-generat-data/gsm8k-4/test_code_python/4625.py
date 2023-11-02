def solution():
    """Alma is taking a walk and comes across four goats standing behind a fence. Alma has a bag of baby carrots she brought to have for a snack and decides to feed the goats with them. Alma wants to make sure all the goats get the same amount of carrots, so she starts counting them out. She has 47 baby carrots. If she wants to give the exact same amount of carrots to each goat and wants to feed them all the carrots she can, how many will she have left over?"""
    # Define the number of baby carrots Alma has
    baby_carrots = 47

    # Define the number of goats
    goats = 4

    # Calculate the number of baby carrots each goat will get
    carrots_per_goat = baby_carrots // goats

    # Calculate the number of baby carrots left over
    leftover_carrots = baby_carrots % goats

    # Return the result
    result = leftover_carrots
    return result

print(solution())