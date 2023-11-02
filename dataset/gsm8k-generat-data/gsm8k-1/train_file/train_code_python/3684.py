def solution():
    """85 paper stars are required to fill a glass jar. Luke has already made 33 stars, but he needs to fill 4 bottles. How many more stars must Luke make?"""
    stars_per_jar = 85
    stars_already_made = 33
    jars_needed = 4
    total_stars_needed = jars_needed * stars_per_jar - stars_already_made
    result = total_stars_needed
    return result

print(solution())