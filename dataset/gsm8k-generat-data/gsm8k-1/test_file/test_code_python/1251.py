def solution():
    """Crista's plants need to be watered every day. She has 20 plants. 4 of her plants need half of a cup of water. 8 plants need 1 cup of water. The rest need a quarter of a cup of water. How many cups of water does Crista need every day for her plants?"""
    total_plants = 20
    half_cup_plants = 4
    one_cup_plants = 8
    quarter_cup_plants = total_plants - half_cup_plants - one_cup_plants
    total_water = (0.5*half_cup_plants) + (1*one_cup_plants) + (0.25*quarter_cup_plants)
    result = total_water
    return result

print(solution())