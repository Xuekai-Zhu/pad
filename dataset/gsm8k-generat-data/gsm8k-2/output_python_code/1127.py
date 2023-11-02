def solution():
    """A certain kind of wild mushroom has either spots or gills, but never both. Gilled mushrooms are rare, with only one growing for every nine spotted mushrooms that grow. A fallen log had 30 mushrooms growing on its side. How many gilled mushrooms were on the fallen log’s side?"""
    total_mushrooms = 30
    spotted_mushrooms = total_mushrooms / 10  # 1 gilled : 9 spotted
    gilled_mushrooms = total_mushrooms - spotted_mushrooms
    result = gilled_mushrooms
    return result

print(solution())