def solution():
    """A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, 
    and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light 
    wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, 
    and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?"""
    # Define the amount of water used for each type of wash
    HEAVY_WASH = 20
    REGULAR_WASH = 10
    LIGHT_WASH = 2

    # Calculate the amount of water needed for the two heavy washes
    heavy_water = HEAVY_WASH * 2

    # Calculate the amount of water needed for the three regular washes
    regular_water = REGULAR_WASH * 3

    # Calculate the amount of water needed for the one light wash
    light_water = LIGHT_WASH

    # Calculate the amount of water needed for the two bleached loads
    bleached_water = (LIGHT_WASH + REGULAR_WASH) * 2

    # Calculate the total amount of water needed
    total_water = heavy_water + regular_water + light_water + bleached_water

    # Display the total amount of water needed
    result = total_water
    return result

print(solution())