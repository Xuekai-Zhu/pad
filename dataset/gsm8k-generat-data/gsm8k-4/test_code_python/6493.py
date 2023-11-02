def solution():
    """Michael is baking a cake and needs 6 cups of flour. The only measuring cup he has is the 1/4 cup. He has an 8 cup bag of flour and realizes it would be faster to measure the flour he doesn't need, take it out of the bag, and then dump the rest of the bag into the bowl. How many scoops should he remove?"""
    # Define the amount of flour needed and the size of the bag
    needed_flour = 6
    bag_size = 8

    # Calculate the amount of flour to be removed
    excess_flour = bag_size - needed_flour

    # Calculate the number of scoops to remove
    scoops_to_remove = excess_flour / 0.25

    # Round up to the nearest whole number
    scoops_to_remove = int(scoops_to_remove + 0.5)

    # Return the result
    result = scoops_to_remove
    return result

print(solution())