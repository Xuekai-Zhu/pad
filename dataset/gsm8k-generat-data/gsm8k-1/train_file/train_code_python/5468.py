def solution():
    """Robby doesn't like the color brown and will not eat the brown M&M's. On his first bag, he sets aside 9 brown M&M's. On the second bag, he sets aside 12. On his third & fourth bag, there are 8 brown M&M's that he doesn't eat. On his fifth bag, there are only 3 brown M&M's that he doesn't eat. What's the average number of brown M&M's in a bag?"""
    brown_mm_per_bag = ((9+12+8+8+3)/5)
    result = brown_mm_per_bag
    return result

print(solution())