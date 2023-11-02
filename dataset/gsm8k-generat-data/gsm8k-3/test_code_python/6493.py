def solution():
    """Michael is baking a cake and needs 6 cups of flour. The only measuring cup he has is the 1/4 cup. He has an 8 cup bag of flour and realizes it would be faster to measure the flour he doesn't need, take it out of the bag, and then dump the rest of the bag into the bowl. How many scoops should he remove?"""
    # Define the amount of flour needed and the size of the bag of flour
    flour_needed = 6
    flour_bag = 8

    # Calculate the amount of flour to be removed
    flour_to_be_removed = flour_bag - flour_needed

    # Calculate the number of scoops to remove
    scoops_to_remove = flour_to_be_removed / 0.25

    # Display the number of scoops to remove
    result = scoops_to_remove
    return result

print(solution())