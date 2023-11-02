def solution():
    # Calculate the number of spruce trees in the forest
    spruces = 0.1 * 4000

    # Calculate the number of pine trees in the forest
    pines = 0.13 * 4000

    # Calculate the number of oak trees in the forest
    oaks = (spruces + pines) / 2

    # Calculate the number of birch trees in the forest
    birches = 4000 - (spruces + pines + oaks)

    result = birches
    return result

print(solution())