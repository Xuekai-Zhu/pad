def solution():
    """Johnny buys 15 packs of colored pencils for his class. Each pack has a red, yellow, and green pencil inside. When he gets home he notices that 3 of the packs have two extra red pencils inside. How many red colored pencils did Johnny buy?"""
    packs = 15
    red_per_pack = 1
    extra_red_packs = 3
    extra_red_per_pack = 2
    total_red = (packs - extra_red_packs) * red_per_pack + extra_red_packs * (red_per_pack + extra_red_per_pack)
    result = total_red
    return result

print(solution())