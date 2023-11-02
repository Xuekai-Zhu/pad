def solution():
    total_water_collected = 65
    water_for_cars = 7 * 2  # 7 gallons each for two cars
    water_for_plants = water_for_cars - 11  # 11 fewer gallons than the cars
    remaining_water = total_water_collected - water_for_cars - water_for_plants  # remaining water after cleaning cars and watering plants
    water_for_washing = remaining_water / 2  # half of remaining water for washing

    result = water_for_washing
    return result

print(solution())