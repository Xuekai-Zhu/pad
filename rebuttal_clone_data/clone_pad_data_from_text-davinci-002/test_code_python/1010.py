def solution():
    bowls_per_minute = 5
    ounces_per_bowl = 10
    gallons_to_soup = 6
    ounces_to_soup = gallons_to_soup * 128
    minutes_to_soup = bowls_per_minute * ounces_per_bowl / ounces_to_soup

    result = minutes_to_soup
    
    return result

print(solution())