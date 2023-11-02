def solution():
    skins_per_coat = 15
    Andy_buys = 30
    babies_per_mink = 6
    total_minks = Andy_buys + babies_per_mink
    half_total_minks = total_minks / 2
    result = half_total_minks * skins_per_coat
    return result

print(solution())