def solution():
    """Becky has 50 necklaces in her jewelry collection. 3 of the necklaces have broken beads so she collects the unbroken beads for crafting and throws the other parts of the 3 the necklaces out. Becky buys 5 new necklaces that week. She decides to give 15 of her old necklaces to her friends as gifts. How many necklaces does she own now?"""
    initial_necklaces = 50
    broken_necklaces = 3
    unbroken_beads_per_necklace = 10
    total_unbroken_beads = (initial_necklaces - broken_necklaces) * unbroken_beads_per_necklace
    new_necklaces = 5
    gifted_necklaces = 15
    total_necklaces = initial_necklaces - broken_necklaces + new_necklaces - gifted_necklaces
    result = total_necklaces
    return result

print(solution())