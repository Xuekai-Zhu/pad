def solution():
    """Alma is taking a walk and comes across four goats standing behind a fence. Alma has a bag of baby carrots she brought to have for a snack and decides to feed the goats with them. Alma wants to make sure all the goats get the same amount of carrots, so she starts counting them out. She has 47 baby carrots. If she wants to give the exact same amount of carrots to each goat and wants to feed them all the carrots she can, how many will she have left over?"""
    num_goats = 4
    num_carrots = 47
    carrots_per_goat = num_carrots // num_goats
    leftovers = num_carrots % num_goats
    result = leftovers
    return result

print(solution())