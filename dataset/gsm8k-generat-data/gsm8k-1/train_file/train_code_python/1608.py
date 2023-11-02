def solution():
    """Kimberly went hiking and took a 4-liter bottle full of water with her. The first time she drank from it, she consumed a quarter of the water in the bottle. Later on, she drank 2/3rd of the remaining water. How much water is left in the bottle (in liters)?"""
    initial_water = 4
    first_drink = initial_water / 4
    remaining_water = initial_water - first_drink
    second_drink = remaining_water * (2/3)
    water_left = remaining_water - second_drink
    result = water_left
    return result

print(solution())