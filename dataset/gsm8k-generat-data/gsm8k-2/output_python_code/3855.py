def solution():
    """Lilith is trying to break the world record for largest cap collection. She collects 3 caps per month in the first year, and 5 caps per month after the first year. Each Christmas, she also receives 40 caps from friends and family. She estimates that each year, she loses 15 of the caps she has collected. If Lilith has been collecting for 5 years, how many caps has she collected so far?"""
    caps_per_year = [3, 5, 5, 5, 5]  # first year = 0th index
    christmas_caps = 40
    lost_caps_per_year = 15
    total_caps = 0
    for i in range(5):
        year_caps = caps_per_year[i] * 12 + christmas_caps - lost_caps_per_year
        total_caps += year_caps

    result = total_caps
    return result

print(solution())