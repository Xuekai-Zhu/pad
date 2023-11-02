def solution():
    # Calculate the remaining water in the tank after evaporation and draining
    remaining_water = 6000 - 2000 - 3500
    
    # Calculate the amount of rain added in 30 minutes
    total_rain = 3 * 350
    
    # Calculate the final amount of water in the tank
    total_water = remaining_water + total_rain
    
    result = total_water
    return result

print(solution())