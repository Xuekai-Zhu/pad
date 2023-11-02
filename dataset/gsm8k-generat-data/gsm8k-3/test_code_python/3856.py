def solution():
    """Lilith is trying to break the world record for largest cap collection. She collects 3 caps per month in the first year, and 5 caps per month after the first year. Each Christmas, she also receives 40 caps from friends and family. She estimates that each year, she loses 15 of the caps she has collected. If Lilith has been collecting for 5 years, how many caps has she collected so far?"""
    # Define the number of caps Lilith collects per month in the first year and after the first year
    FIRST_YEAR_CAPS = 3
    AFTER_FIRST_YEAR_CAPS = 5

    # Define the number of caps Lilith receives each Christmas and loses each year
    CHRISTMAS_CAPS = 40
    LOST_CAPS_PER_YEAR = 15

    # Calculate the total number of caps Lilith collects in the first year
    first_year_caps = FIRST_YEAR_CAPS * 12

    # Calculate the total number of caps Lilith collects in the following years
    after_first_year_caps = AFTER_FIRST_YEAR_CAPS * 12 * 4

    # Calculate the total number of caps Lilith receives from Christmas
    christmas_caps = CHRISTMAS_CAPS * 5

    # Calculate the total number of caps Lilith loses in 5 years
    lost_caps = LOST_CAPS_PER_YEAR * 5

    # Calculate the total number of caps Lilith has collected so far
    total_caps = first_year_caps + after_first_year_caps + christmas_caps - lost_caps

    # Display the total number of caps
    result = total_caps
    return result

print(solution())