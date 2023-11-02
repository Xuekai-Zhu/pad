def solution():
    """Tabitha adds 1 serving of honey per cup of tea in the evening.  She usually has 2 cups of tea before bed.  She buys her honey in a 16-ounce container.  If there are 6 servings of honey per ounce, how many nights will she be able to enjoy honey in her tea before bed?"""
    # Define the amount of honey per serving in ounces
    HONEY_PER_SERVING = 1/6

    # Define the number of cups of tea Tabitha drinks before bed
    cups_per_night = 2

    # Calculate the amount of honey used per night
    honey_per_night = cups_per_night * HONEY_PER_SERVING

    # Define the size of the honey container in ounces
    honey_container_size = 16

    # Calculate the number of nights Tabitha can enjoy honey in her tea before running out
    nights_of_honey = honey_container_size / honey_per_night

    # Display the number of nights Tabitha can enjoy honey
    result = nights_of_honey
    return result

print(solution())