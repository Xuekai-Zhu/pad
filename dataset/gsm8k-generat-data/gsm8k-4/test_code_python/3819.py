def solution():
    """Becky has 50 necklaces in her jewelry collection. 3 of the necklaces have broken beads so she collects the unbroken beads for crafting and throws the other parts of the 3 the necklaces out. Becky buys 5 new necklaces that week. She decides to give 15 of her old necklaces to her friends as gifts. How many necklaces does she own now?"""
    # Define the initial number of necklaces
    initial_necklaces = 50

    # Remove the broken necklaces
    necklaces_after_broken = initial_necklaces - 3

    # Add the new necklaces
    necklaces_after_new = necklaces_after_broken + 5

    # Remove the gifted necklaces
    necklaces_after_gifted = necklaces_after_new - 15

    # return the result
    result = necklaces_after_gifted
    return result

print(solution())