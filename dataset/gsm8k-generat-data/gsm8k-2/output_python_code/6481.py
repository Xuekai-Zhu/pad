def solution():
    """Tiffany is looking at a lake full of turtles. The turtles are 60% female and the rest are male. Of the males, 1 in 4 has stripes. Of the ones with stripes, 4 are babies, while 60% are adults How many turtles are in the lake?"""
    female_turtles_ratio = 0.6
    male_turtles_ratio = 1 - female_turtles_ratio
    striped_male_ratio = 0.25 * male_turtles_ratio
    total_babies_with_stripes = 4
    total_adults_with_stripes = striped_male_ratio * 0.6
    total_striped_male_turtles = total_babies_with_stripes + total_adults_with_stripes
    total_turtles = 1 / (female_turtles_ratio + male_turtles_ratio)
    total_females = female_turtles_ratio * total_turtles
    total_males = male_turtles_ratio * total_turtles
    result = total_turtles
    return result

print(solution())