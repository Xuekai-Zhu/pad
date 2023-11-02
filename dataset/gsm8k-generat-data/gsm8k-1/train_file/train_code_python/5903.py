def solution():
    """Bill and Phil are firehouse Dalmatians. Bill has one less than twice as many spots as Phil. If they have 59 spots combined, how many spots does Bill have?"""
    total_spots = 59
    # Let's set up an equation to represent the given information
    # We know that Bill has one less than twice as many spots as Phil, so:
    # b = 2p - 1, where b is the number of spots Bill has and p is the number of spots Phil has
    # We also know that their total number of spots is 59, so:
    # b + p = 59
    # Now we can substitute the first equation into the second equation and solve for p:
    # (2p - 1) + p = 59
    # 3p - 1 = 59
    # 3p = 60
    # p = 20
    # Now that we know Phil has 20 spots, we can use the first equation to find that Bill has:
    # b = 2p - 1
    # b = 2(20) - 1
    # b = 39
    result = 39
    return result

print(solution())