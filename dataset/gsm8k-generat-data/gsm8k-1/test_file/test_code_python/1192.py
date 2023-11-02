def solution():
    """Alain's mom bought 5 packs of red pens and also bought twice the amount of black pens than the red. If each pack has 5 pens, how many pens does Alain have?"""
    red_packs = 5
    black_packs = red_packs * 2
    pens_per_pack = 5
    total_pens = (red_packs + black_packs) * pens_per_pack
    result = total_pens
    return result

print(solution())