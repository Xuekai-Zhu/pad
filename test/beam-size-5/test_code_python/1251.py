def solution():
    total_plants = 20  # Crista has 20 plants
    half_plants = 4  # 4 plants need half of a cup of water
    one_plant = 8  # 8 plants need 1 cup of water
    quarter_plants = total_plants - half_plants - one_plant  # The rest need a quarter of a cup of water

    # Calculate the total cups of water needed for all the plants
    total_water = (half_plants * 0.5) + (one_plant * 0.25)
    result = total_water
    return result

print(solution())