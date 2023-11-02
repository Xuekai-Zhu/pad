def solution():
    pump_rate = 3  # Casey can pump 3 gallons of water per minute
    corn_plants = 4 * 15  # Casey has 4 rows of 15 corn plants each
    corn_water = 0.5 * corn_plants  # each corn plant needs half a gallon of water
    pig_water = 10 * 4  # Casey has 10 pigs, each needing 4 gallons of water
    duck_water = 20 * 0.25  # Casey has 20 ducks, each needing a quarter of a gallon of water
    total_water = corn_water + pig_water + duck_water  # Total water needed

    # Calculate the time Casey needs to spend pumping water
    time_needed = total_water / pump_rate
    result = time_needed
    return result

print(solution())