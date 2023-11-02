def solution():
    """A certain kind of wild mushroom has either spots or gills, but never both. Gilled mushrooms are rare, with only one growing for every nine spotted mushrooms that grow. A fallen log had 30 mushrooms growing on its side. How many gilled mushrooms were on the fallen log’s side?"""
    total_mushrooms = 30
    ratio_gilled = 1/10   # one gilled mushroom for every 9 spotted mushrooms
    gilled_mushrooms = total_mushrooms * ratio_gilled
    result = gilled_mushrooms
    return result

print(solution())