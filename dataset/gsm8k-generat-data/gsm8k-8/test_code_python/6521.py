def solution():
    # Calculate the number of spruces and pines
    spruces = 0.1 * 4000
    pines = 0.13 * 4000

    # Calculate the number of oaks
    oaks = spruces + pines

    # Calculate the number of birches
    birches = 4000 - spruces - pines - oaks
    result = birches
    return result

print(solution())