def solution():
    """Casey is pumping water out of her well. She can pump 3 gallons a minute. She has 4 rows of 15 corn plants each, and each plant needs half a gallon of water. She also has 10 pigs, which each need 4 gallons of water, and 20 ducks that each need a quarter of a gallon of water. How many minutes does Casey need to spend pumping water?"""
    corn_rows = 4
    corn_plants_per_row = 15
    water_per_plant = 0.5
    pig_count = 10
    water_per_pig = 4
    duck_count = 20
    water_per_duck = 0.25

    total_water_needed = (corn_rows * corn_plants_per_row * water_per_plant) + (pig_count * water_per_pig) + (
                duck_count * water_per_duck)
    minutes_needed = total_water_needed / 3 # since Casey can pump 3 gallons a minute
    result = minutes_needed
    return result

print(solution())