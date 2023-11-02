def solution():
    """John buys 2 packs of gum and 3 candy bars. Each stick of gum cost half as much as the candy bar. If the candy bar cost $1.5 each, how much did he pay in total?"""
    # Define the number of gum packs and candy bars purchased
    gum_packs = 2
    candy_bars = 3

    # Define the cost of one candy bar and calculate the cost of one stick of gum
    candy_bar_cost = 1.5
    gum_cost = candy_bar_cost / 2

    # Calculate the total cost of the gum packs and candy bars
    total_cost = (gum_cost * 2) + (candy_bar_cost * 3)

    result = total_cost
    return result

print(solution())