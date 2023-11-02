def solution():
    """Tabitha adds 1 serving of honey per cup of tea in the evening. She usually has 2 cups of tea before bed. She buys her honey in a 16-ounce container. If there are 6 servings of honey per ounce, how many nights will she be able to enjoy honey in her tea before bed?"""
    # Define the number of cups of tea per night
    cups_per_night = 2
    
    # Define the size of the honey container in ounces
    honey_container = 16
    
    # Define the number of servings of honey per ounce
    servings_per_ounce = 6
    
    # Calculate the number of servings of honey used per night
    servings_per_night = cups_per_night
    
    # Calculate the number of ounces of honey used per night
    ounces_per_night = servings_per_night / servings_per_ounce
    
    # Calculate the number of nights the honey will last
    nights = honey_container / ounces_per_night
    
    # Round down to the nearest whole number of nights
    nights = int(nights)
    
    # Return the result
    result = nights
    return result

print(solution())