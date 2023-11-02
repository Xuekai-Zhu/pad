def solution():
    """Tiffany is looking at a lake full of turtles. The turtles are 60% female and the rest are male. Of the males, 1 in 4 has stripes. Of the ones with stripes, 4 are babies, while 60% are adults. How many turtles are in the lake?"""
    # Define the percentage of female turtles
    female_percentage = 0.6

    # Calculate the percentage of male turtles
    male_percentage = 1 - female_percentage

    # Calculate the percentage of male turtles with stripes
    striped_male_percentage = male_percentage / 4

    # Calculate the percentage of striped male turtles that are adults
    adult_striped_male_percentage = striped_male_percentage * 0.6

    # Calculate the percentage of striped male turtles that are babies
    baby_striped_male_percentage = striped_male_percentage * 0.4

    # Calculate the percentage of turtles that are adult females
    adult_female_percentage = female_percentage * 0.6

    # Calculate the percentage of turtles that are adult males
    adult_male_percentage = male_percentage * 0.6

    # Calculate the total percentage of adult turtles
    adult_percentage = adult_female_percentage + adult_male_percentage + adult_striped_male_percentage

    # Calculate the total number of turtles in the lake
    total_turtles = 100 / adult_percentage

    result = round(total_turtles)
    return result

print(solution())