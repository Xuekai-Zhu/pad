def solution():
    """Michael is baking a cake and needs 6 cups of flour. The only measuring cup he has is the 1/4 cup. He has an 8 cup bag of flour and realizes it would be faster to measure the flour he doesn't need, take it out of the bag, and then dump the rest of the bag into the bowl. How many scoops should he remove?"""
    cups_needed = 6
    cups_per_scoop = 0.25
    total_cups = 8
    cups_to_remove = total_cups - cups_needed
    scoops_to_remove = int(cups_to_remove / cups_per_scoop)
    result = scoops_to_remove
    return result

print(solution())