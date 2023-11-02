def solution():
    """The rainy season is here, Jan collected 65 gallons of water in a barrel outside her home. She uses 7 gallons of water each to clean the two cars and uses 11 fewer gallons than the two cars to water the plants. Then, she uses half of the remaining gallons of water to wash the plates and clothes. How many gallons of water does Jan use to wash her plates and clothes?"""
    total_water = 65
    car_cleaning_water = 7 * 2
    plant_water = car_cleaning_water - 11
    remaining_water = total_water - car_cleaning_water - plant_water
    plate_clothes_water = remaining_water / 2
    result = plate_clothes_water
    return result

print(solution())