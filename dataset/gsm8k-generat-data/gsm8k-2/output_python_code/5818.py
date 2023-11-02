def solution():
    """Casey is pumping water out of her well. She can pump 3 gallons a minute. She has 4 rows of 15 corn plants each, and each plant needs half a gallon of water. She also has 10 pigs, which each need 4 gallons of water, and 20 ducks that each need a quarter of a gallon of water. How many minutes does Casey need to spend pumping water?"""
    corn_plants = 4 * 15
    corn_water_needed = corn_plants * 0.5
    pig_water_needed = 10 * 4
    duck_water_needed = 20 * 0.25
    total_water_needed = corn_water_needed + pig_water_needed + duck_water_needed
    pump_speed = 3
    pumping_time = total_water_needed / pump_speed
    result = pumping_time
    return result

print(solution())