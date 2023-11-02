def solution():
    gallons_per_minute = 3
    corn_plants = 4 * 15
    water_per_corn_plant = 0.5
    total_water_for_corn = corn_plants * water_per_corn_plant
    pigs = 10
    water_per_pig = 4
    total_water_for_pigs = pigs * water_per_pig
    ducks = 20
    water_per_duck = 0.25
    total_water_for_ducks = ducks * water_per_duck
    total_water_needed = total_water_for_corn + total_water_for_pigs + total_water_for_ducks
    minutes_needed = total_water_needed / gallons_per_minute
    return result

print(solution())