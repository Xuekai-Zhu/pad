def solution():
    """Lilith is trying to break the world record for largest cap collection. She collects 3 caps per month in the first year, and 5 caps per month after the first year. Each Christmas, she also receives 40 caps from friends and family. She estimates that each year, she loses 15 of the caps she has collected. If Lilith has been collecting for 5 years, how many caps has she collected so far?"""
    # Define the number of caps collected in the first year
    first_year_caps = 3 * 12

    # Define the number of caps collected in the following years
    following_years_caps = (5 * 12) * 4
    
    # Define the number of caps from Christmas gifts
    christmas_caps = 40 * 5

    # Define the number of caps lost each year
    caps_lost_yearly = 15 * 5

    # Calculate the total number of caps collected
    total_caps_collected = first_year_caps + following_years_caps + christmas_caps - caps_lost_yearly

    # return the result
    result = total_caps_collected
    return result

print(solution())