def solution():
    """Bill and Phil are firehouse Dalmatians. Bill has one less than twice as many spots as Phil. If they have 59 spots combined, how many spots does Bill have?"""
    # Let x be the number of spots on Phil
    # Then Bill has 2x-1 spots
    # We know that x + 2x-1 = 59
    # Simplifying, we get 3x = 60, so x = 20
    # Therefore, Bill has 2(20)-1 = 39 spots

    bill_spots = 2*20-1
    result = bill_spots
    return result

print(solution())