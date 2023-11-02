def solution():
    """Daniel has 5 jars of juice containing 2 liters each. He wants to serve a full glass of juice to each person at a party. He knows that each glass can hold up to 250 milliliters of juice. How many full glasses can he give?"""
    # Define the total amount of juice in liters and the volume of each glass in milliliters
    JUICE_VOLUME = 2 * 5
    GLASS_VOLUME = 250

    # Convert the juice volume to milliliters
    juice_volume_ml = JUICE_VOLUME * 1000

    # Divide the juice volume by the glass volume to get the number of glasses
    num_glasses = juice_volume_ml // GLASS_VOLUME

    # Display the number of glasses
    result = num_glasses
    return result

print(solution())