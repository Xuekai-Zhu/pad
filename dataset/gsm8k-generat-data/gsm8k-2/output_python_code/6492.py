def solution():
    """Michael is baking a cake and needs 6 cups of flour. The only measuring cup he has is the 1/4 cup. He has an 8 cup bag of flour and realizes it would be faster to measure the flour he doesn't need, take it out of the bag, and then dump the rest of the bag into the bowl. How many scoops should he remove?"""
    needed_flour = 6
    measuring_cup_size = 0.25
    total_flour = 8
    scoops_to_remove = (total_flour - needed_flour) // measuring_cup_size
    result = scoops_to_remove
    return result

print(solution())