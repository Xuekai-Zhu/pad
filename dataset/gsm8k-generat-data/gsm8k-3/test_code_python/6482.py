def solution():
    """Tiffany is looking at a lake full of turtles. The turtles are 60% female and the rest are male. Of the males, 1 in 4 has stripes. Of the ones with stripes, 4 are babies, while 60% are adults How many turtles are in the lake?"""
    # Define the percentage of female turtles and calculate the percentage of male turtles
    FEMALE_PERCENTAGE = 60
    MALE_PERCENTAGE = 100 - FEMALE_PERCENTAGE

    # Calculate the number of male turtles
    total_turtles = 100  # Assume 100 turtles in the lake
    male_turtles = MALE_PERCENTAGE/100 * total_turtles

    # Calculate the number of male turtles with stripes
    striped_turtles = 1/4 * male_turtles

    # Calculate the number of adult striped turtles
    adult_striped_turtles = 60/100 * striped_turtles

    # Calculate the total number of turtles in the lake
    female_turtles = FEMALE_PERCENTAGE/100 * total_turtles
    baby_turtles = 4
    total_turtles = female_turtles + male_turtles + baby_turtles + adult_striped_turtles

    # Display the total number of turtles
    result = total_turtles
    return result

print(solution())