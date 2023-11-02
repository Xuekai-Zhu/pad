def solution():
    """Robby doesn't like the color brown and will not eat the brown M&M's.  On his first bag, he sets aside  9 brown M&M's.  On the second bag, he sets aside 12.  On his third & fourth bag, there are 8 brown M&M's that he doesn't eat. On his fifth bag, there are only 3 brown M&M's that he doesn't eat.  What's the average number of brown M&M's in a bag?"""
    # Define the number of brown M&M's in each bag
    bag1 = 9
    bag2 = 12
    bag3 = 8
    bag4 = 8
    bag5 = 3

    # Calculate the total number of brown M&M's and bags
    total_brown = bag1 + bag2 + bag3 + bag4 + bag5
    num_bags = 5

    # Calculate the average number of brown M&M's per bag
    avg_brown_per_bag = total_brown / num_bags

    # Display the average number of brown M&M's per bag
    result = avg_brown_per_bag
    return result

print(solution())