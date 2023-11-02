def solution():
    
    own_packs = 3
    neighbor_packs = 2
    balloons_per_pack = 6
    total_balloons = (own_packs + neighbor_packs) * balloons_per_pack
    floretta_balloons = total_balloons / 2
    floretta_balloons -= 7
    result = floretta_balloons
    return result

print(solution())