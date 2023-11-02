def solution():
    """Robby doesn't like the color brown and will not eat the brown M&M's. On his first bag, he sets aside 9 brown M&M's. On the second bag, he sets aside 12. On his third & fourth bag, there are 8 brown M&M's that he doesn't eat. On his fifth bag, there are only 3 brown M&M's that he doesn't eat. What's the average number of brown M&M's in a bag?"""
    # Calculate the total number of brown M&M's set aside
    total_brown_mms = 9 + 12 + 8*2 + 3

    # Calculate the total number of bags
    total_bags = 5

    # Calculate the average number of brown M&M's per bag
    avg_brown_mms = total_brown_mms / total_bags

    result = avg_brown_mms
    return result

print(solution())