def solution():
    
    # Define the minimum temperature Donny can drink water
    MIN_TEMP = 40

    # Define the number of mugs of water Donny has
    num_mugs = 2

    # Define the temperature of the mug of water
    mug_temp = 33

    # Calculate the total temperature of the water Donny has
    total_temp = num_mugs * mug_temp

    # Calculate the amount of water Donny pours into his water bottle
    water_bottle_pour = 4

    # Calculate the amount of water Donny pours into his water bottle
    water_bottle_pour = total_temp - water_bottle_pour

    # Calculate the minimum temperature of the second bottle
    water_bottle_max = water_bottle_pour / MIN_TEMP

    # Display the minimum temperature of the second bottle
    result = water_bottle_max
    return result

print(solution())