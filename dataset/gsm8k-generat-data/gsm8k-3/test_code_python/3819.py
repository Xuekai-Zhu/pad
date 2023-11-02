def solution():
    """Becky has 50 necklaces in her jewelry collection. 3 of the necklaces have broken beads so she collects the unbroken beads for crafting and throws the other parts of the 3 the necklaces out. Becky buys 5 new necklaces that week. She decides to give 15 of her old necklaces to her friends as gifts. How many necklaces does she own now?"""
    # Initial number of necklaces
    initial_necklaces = 50

    # Number of necklaces with broken beads
    broken_necklaces = 3

    # Number of unbroken beads collected
    unbroken_beads = (initial_necklaces - broken_necklaces) * 15

    # Total number of necklaces after collecting unbroken beads
    new_necklaces = initial_necklaces - broken_necklaces + unbroken_beads + 5 - 15

    # Display the total number of necklaces
    result = new_necklaces
    return result

print(solution())