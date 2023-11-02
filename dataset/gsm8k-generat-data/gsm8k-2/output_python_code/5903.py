def solution():
    """Bill and Phil are firehouse Dalmatians. Bill has one less than twice as many spots as Phil. If they have 59 spots combined, how many spots does Bill have?"""
    total_spots = 59
    # Let's assume that Phil has x spots
    x = 0
    # We know that Bill has one less than twice as many spots as Phil
    # So we can write Bill's spots in terms of x
    bill_spots = 2*x - 1
    # We also know that the total spots is the sum of their spots
    # So we can write an equation in terms of x and solve for x
    x = (total_spots + 1) / 3
    # Now that we know x, we can find Bill's spots
    bill_spots = 2*x - 1
    result = bill_spots
    return result

print(solution())