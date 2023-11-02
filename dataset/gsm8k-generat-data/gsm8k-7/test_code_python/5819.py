def solution():
    water_needed_for_corn_plants = 15 * 4 * 0.5  # 15 plants per row, 4 rows, each plant needs half a gallon
    water_needed_for_pigs = 10 * 4  # 10 pigs each need 4 gallons of water
    water_needed_for_ducks = 20 * 0.25  # 20 ducks each need a quarter of a gallon of water

    total_water_needed = water_needed_for_corn_plants + water_needed_for_pigs + water_needed_for_ducks

    minutes_to_pump_all_water = total_water_needed / 3  # Casey can pump 3 gallons a minute

    result = minutes_to_pump_all_water
    return result

print(solution())