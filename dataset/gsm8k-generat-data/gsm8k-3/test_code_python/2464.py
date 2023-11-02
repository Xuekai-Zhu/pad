def solution():
    """A mother is making her own bubble mix out of dish soap and water for her two-year-old son.  The recipe she is following calls for 3 tablespoons of soap for every 1 cup of water.  If the container she hopes to store the bubble mix in can hold 40 ounces of liquid, and there are 8 ounces in a cup of water, how many tablespoons of soap should she add to the container (assuming that the soap itself doesn't count towards the capacity of the container)?"""
    # Define the soap-water ratio
    SOAP_TO_WATER = 3 / 1

    # Define the volume of the container in cups
    CONTAINER_VOLUME = 40 / 8

    # Calculate the volume of water needed
    water_volume = CONTAINER_VOLUME / (1 + SOAP_TO_WATER)

    # Calculate the volume of soap needed
    soap_volume = SOAP_TO_WATER * water_volume

    # Calculate the amount of soap in tablespoons
    soap_in_tablespoons = soap_volume * 2 * 3

    # Display the number of tablespoons of soap needed
    result = soap_in_tablespoons
    return result

print(solution())