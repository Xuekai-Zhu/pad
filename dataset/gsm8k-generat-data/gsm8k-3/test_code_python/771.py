def solution():
    """Jimmy decides to make sandwiches for a picnic.  He makes 8 sandwiches in total, using two slices of bread each.  How many packs of bread does he need to buy to make these sandwiches, assuming he starts with no bread and each pack has 4 slices of bread in it?"""
    # Calculate the total number of slices of bread needed
    slices_needed = 8 * 2

    # Calculate the number of packs of bread needed
    packs_needed = slices_needed / 4

    # Round up to the nearest whole pack
    packs_needed = math.ceil(packs_needed)

    # Display the number of packs needed
    result = packs_needed
    return result

print(solution())