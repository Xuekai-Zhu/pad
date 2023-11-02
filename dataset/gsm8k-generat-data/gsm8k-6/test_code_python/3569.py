def solution():
    # Calculate the remaining liters of water in the tank after evaporation and drainage
    remaining_liters = 6000 - 2000 - 3500  

    # Calculate the total liters of rain that will be added in 30 minutes
    total_rain_liters = 3 * 350  # 3 cycles of 10 minutes each

    # Calculate the final liters of water in the tank
    final_liters = remaining_liters + total_rain_liters
    result = final_liters
    return result

print(solution())