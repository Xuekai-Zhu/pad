def solution():
    total_water = 4  # Kimberly started with a 4-liter bottle of water
    first_drink = total_water / 4  # Kimberly drank a quarter of the water
    remaining_water = total_water - first_drink  # Calculate how much water is left after the first drink
    second_drink = remaining_water * (2 / 3)  # Kimberly drank 2/3rd of the remaining water
    total_drinks = first_drink + second_drink  # Calculate the total amount of water Kimberly drank
    water_left = total_water - total_drinks  # Calculate how much water is left in the bottle
    result = water_left
    return result

print(solution())