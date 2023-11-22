def solution():
    
    # Define the number of spools of each color
    light_blue = 15
    dark_blue = 45
    light_green = 40
    dark_green = 50

    # Calculate the total number of spools
    total_spools = light_blue + dark_blue + light_green + dark_green

    # Calculate the percentage of spools that are blue
    blue_percentage = (light_blue / total_spools) * 100

    # Display the percentage of spools that are blue
    result = blue_percentage
    return result

print(solution())