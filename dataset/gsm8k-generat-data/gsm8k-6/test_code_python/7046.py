def solution():
    # Calculate the gallons of water used for cars and plants
    car_water = 2 * 7  # Jan uses 7 gallons of water each to clean the two cars
    plant_water = car_water - 11  # Jan uses 11 fewer gallons than the two cars to water the plants
    
    # Calculate the remaining gallons of water after using for cars and plants
    remaining_water = 65 - car_water - plant_water
    
    # Calculate the gallons of water used to wash plates and clothes
    wash_water = remaining_water / 2  # Jan uses half of the remaining gallons of water to wash the plates and clothes
    
    result = wash_water
    return result

print(solution())