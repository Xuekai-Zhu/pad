def solution():
    """Albert noticed a flock of geese flying together in a V formation in the sky overhead.  One half of the geese broke off from the formation, flew toward the earth, and landed in some trees.  Then, 4 geese flew up, out of the trees, and joined those already flying in the air to make a new V formation in the sky.  If the final number of geese flying in the V formation was 12, how many geese were in the first formation Albert noticed in the sky?"""
    # Let x be the total number of geese in the first formation
    # Half of them flew to the trees, so there were x/2 geese left in the sky
    # 4 geese flew up from the trees to join the remaining geese, so there were x/2 + 4 geese in the second formation
    # The total number of geese in the second formation was 12, so we can write an equation:
    # x/2 + 4 = 12
    # Solving for x:
    x = (12 - 4) * 2
    result = x
    return result

print(solution())