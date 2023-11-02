def solution():
    """The rainy season is here, Jan collected 65 gallons of water in a barrel outside her home. She uses 7 gallons of water each to clean the two cars and uses 11 fewer gallons than the two cars to water the plants. Then, she uses half of the remaining gallons of water to wash the plates and clothes. How many gallons of water does Jan use to wash her plates and clothes?"""
    total_gallons = 65
    cars_water = 2 * 7
    plant_water = cars_water - 11
    remaining_gallons = total_gallons - cars_water - plant_water
    plates_clothes_water = remaining_gallons / 2
    result = plates_clothes_water
    return result

print(solution())