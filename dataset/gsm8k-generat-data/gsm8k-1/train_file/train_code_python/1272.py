def solution():
    """John buys 2 packs of gum and 3 candy bars. Each stick of gum cost half as much as the candy bar. If the candy bar cost $1.5 each, how much did he pay in total?"""
    gum_packs = 2
    candy_bars = 3
    gum_cost = 0.5 * 1.5  # the cost of one candy bar
    total_cost = (gum_packs * 2 * gum_cost) + (candy_bars * 1.5)
    result = total_cost
    return result

print(solution())