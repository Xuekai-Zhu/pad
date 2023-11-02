def solution():
    total_drinks = 54  # Carla drank 54 ounces of liquid in total
    soda = (total_drinks - 6) / 4  # Carla drank three times as much soda minus 6 ounces as water
    water = total_drinks - soda  # Calculate the amount of water Carla drank
    result = water
    return result

print(solution())