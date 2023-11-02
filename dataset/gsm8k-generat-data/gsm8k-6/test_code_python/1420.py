def solution():
    total = 54  # total ounces of liquid Carla drank
    soda = (3 * water) - 6  # ounces of soda Carla drank, in terms of water
    water = (total - soda) / 4  # ounces of water Carla drank, in 4 parts (3 parts soda and 1 part water)
    result = water
    return result

print(solution())