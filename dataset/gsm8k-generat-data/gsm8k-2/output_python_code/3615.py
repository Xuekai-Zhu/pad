def solution():
    """Cornelia likes to travel. She visited already 42 different countries. 20 of them were in Europe and 10 in South America. From the rest of the countries, only half of them were in Asia. How many Asian countries has Cornelia visited?"""
    total_countries = 42
    europe_countries = 20
    south_america_countries = 10
    rest_countries = total_countries - europe_countries - south_america_countries
    asia_countries = rest_countries / 2
    result = asia_countries
    return result

print(solution())