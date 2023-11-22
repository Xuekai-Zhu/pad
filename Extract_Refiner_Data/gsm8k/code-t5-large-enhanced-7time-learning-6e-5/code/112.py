def solution():
    
    # Define the ratio of sugar to water
    sugar_to_water_ratio = 7/13

    # Calculate the total ratio
    total_ratio = 7 + 13

    # Calculate the amount of sugar used
    sugar_used = (sugar_to_water_ratio / total_ratio) * 120

    # Calculate the amount of teaspoonfuls of sugar used
    sugar_used = sugar_used / 7

    # Display the number of teaspoonfuls of sugar used
    result = sugar_used
    return result

print(solution())