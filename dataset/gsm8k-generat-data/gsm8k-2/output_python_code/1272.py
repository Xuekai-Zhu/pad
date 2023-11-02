def solution():
    """John buys 2 packs of gum and 3 candy bars. Each stick of gum cost half as much as the candy bar. If the candy bar cost $1.5 each, how much did he pay in total?"""
    gum_price = 1.5 / 2
    candy_price = 1.5
    total_price = (2 * gum_price) + (3 * candy_price)
    result = total_price
    return result

print(solution())