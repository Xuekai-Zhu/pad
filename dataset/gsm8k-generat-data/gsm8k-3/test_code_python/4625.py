def solution():
    """Alma is taking a walk and comes across four goats standing behind a fence. Alma has a bag of baby carrots she brought to have for a snack and decides to feed the goats with them. Alma wants to make sure all the goats get the same amount of carrots, so she starts counting them out. She has 47 baby carrots. If she wants to give the exact same amount of carrots to each goat and wants to feed them all the carrots she can, how many will she have left over?"""
    # Define the number of goats and the number of carrots
    NUM_GOATS = 4
    NUM_CARROTS = 47

    # Calculate the number of carrots each goat will get
    carrots_per_goat = NUM_CARROTS // NUM_GOATS

    # Calculate the number of carrots left over
    carrots_left_over = NUM_CARROTS % NUM_GOATS

    # Display the number of carrots left over
    result = carrots_left_over
    return result

print(solution())