def solution():
    gum_packs = 2
    candy_bars = 3
    gum_per_pack = 10
    candy_bar_cost = 1.5
    gum_cost = gum_packs * (gum_per_pack / 2) * candy_bar_cost
    total_cost = gum_cost + (candy_bars * candy_bar_cost)
    result = total_cost
    return result

print(solution())