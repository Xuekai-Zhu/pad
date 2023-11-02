def solution():
    total_trees = 4000  # Total number of trees in the forest
    spruces = total_trees * 0.1  # Number of spruces (10% of total trees)
    pines = total_trees * 0.13  # Number of pines (13% of total trees)
    oaks = (spruces + pines) / 2  # Number of oaks (same as spruces and pines combined)

    # Calculate the number of birches in the forest
    birches = total_trees - spruces - pines - oaks

    result = birches
    return result

print(solution())