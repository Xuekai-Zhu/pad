def solution():
    """It takes 15 mink skins to make a coat. Andy buys 30 minks and each mink has 6 babies, but half the total minks are set free by activists. How many coats can he make?"""
    skins_per_coat = 15
    andy_minks = 30
    andy_minks_babies = andy_minks * 6
    total_minks = andy_minks + andy_minks_babies
    total_minks = int(total_minks / 2)  # half of total minks are set free
    total_coats = int(total_minks / skins_per_coat)
    result = total_coats
    return result

print(solution())