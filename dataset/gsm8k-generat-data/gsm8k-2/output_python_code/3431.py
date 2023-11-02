def solution():
    """Milly and Floretta are having a water balloon fight in their garden. They use 3 packs of their own water balloons and also use 2 packs of a neighbor’s water balloons. Each pack of water balloons contains 6 balloons. Milly and Floretta fill all of the balloons then split them evenly, but Milly takes an extra 7 balloons when Floretta isn't looking. How many water balloons is Floretta left with?"""
    own_packs = 3
    neighbor_packs = 2
    balloons_per_pack = 6
    total_balloons = (own_packs + neighbor_packs) * balloons_per_pack
    floretta_balloons = total_balloons // 2
    milly_balloons = floretta_balloons + 7
    floretta_balloons = (total_balloons - milly_balloons) // 2
    result = floretta_balloons
    return result

print(solution())