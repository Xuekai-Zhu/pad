def solution():
    """Jimmy decides to make sandwiches for a picnic. He makes 8 sandwiches in total, using two slices of bread each. How many packs of bread does he need to buy to make these sandwiches, assuming he starts with no bread and each pack has 4 slices of bread in it?"""
    sandwiches = 8
    slices_per_sandwich = 2
    slices_needed = sandwiches * slices_per_sandwich
    slices_per_pack = 4
    packs_needed = slices_needed / slices_per_pack
    result = packs_needed
    return result

print(solution())