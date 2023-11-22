def solution():
    
    # Define the initial temperature and the additional temperature
    INITIAL_TEMP = 13
    ADDITIONAL_TEMP = 15

    # Calculate the total temperature and additional temperature
    total_temp = INITIAL_TEMP + ADDITIONAL_TEMP

    # Calculate the weight of the ice cubes
    weight_cube = total_temp // INITIAL_TEMP

    # Calculate the weight of the ice cubes
    weight_ice_cubes = weight_cube * 3

    # Calculate the weight of the ice cubes with the added liquid
    weight_liquid = weight_cube + ADDITIONAL_TEMP

    # Calculate the total weight of the iced coffee
    total_weight = weight_cube + weight_liquid

    # Display the total weight of the iced coffee
    result = total_weight
    return result

print(solution())