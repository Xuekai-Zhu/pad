def solution():
    
    # Define the ratio of sugar to cups of water
    SUGAR_TO_WATER_RATIO = 7/13

    # Calculate the total amount of water used
    total_water_used = 120 / (SUGAR_TO_WATER_RATIO + 13)

    # Calculate the number of teaspoonfuls of sugar used
    sugar_used = total_water_used / SUGAR_TO_WATER_RATIO

    # Display the number of teaspoonfuls of sugar used
    result = sugar_used
    return result

print(solution())