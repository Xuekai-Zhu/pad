def solution():
    pack1 = 6
    pack2 = 6
    pack3 = 6
    pack4 = 6
    pack5 = 6
    packs_of_balloons = pack1 + pack2 + pack3 + pack4 + pack5
    total_balloons = packs_of_balloons * 3
    milled_stole = 7
    floretta_has = total_balloons - milled_stole
    result = floretta_has
    return result

print(solution())