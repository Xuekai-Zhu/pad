def solution():
    """Lilith is trying to break the world record for largest cap collection. She collects 3 caps per month in the first year, and 5 caps per month after the first year. Each Christmas, she also receives 40 caps from friends and family. She estimates that each year, she loses 15 of the caps she has collected. If Lilith has been collecting for 5 years, how many caps has she collected so far?"""
    
    # Calculate total caps collected in first year
    first_year = 3 * 12
    
    # Calculate total caps collected in remaining four years
    remaining_years = (5 * 12 - 12) * 5
    
    # Calculate total caps received from friends and family
    christmas_caps = 40 * 5
    
    # Calculate total caps lost each year
    total_lost = 15 * 5
    
    # Calculate total caps collected
    total_collected = first_year + remaining_years + christmas_caps - total_lost
    
    result = total_collected
    return result

print(solution())