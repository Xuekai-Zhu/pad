def solution():
    """Anna goes trick-or-treating in a subdivision where she gets 14 pieces of candy per house. Her brother Billy goes trick-or-tricking in a neighboring subdivision where he gets 11 pieces of candy per house. If the first subdivision has 60 houses and the second subdivision has 75 houses, how many more pieces of candy does Anna get?"""
    candy_per_house_anna = 14
    candy_per_house_billy = 11
    houses_anna = 60
    houses_billy = 75
    candy_anna = candy_per_house_anna * houses_anna
    candy_billy = candy_per_house_billy * houses_billy
    difference = candy_anna - candy_billy
    result = difference
    return result

print(solution())