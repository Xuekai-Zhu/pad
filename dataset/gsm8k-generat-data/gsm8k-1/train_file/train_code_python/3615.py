def solution():
    """Cornelia likes to travel. She visited already 42 different countries. 20 of them were in Europe and 10 in South America. From the rest of the countries, only half of them were in Asia. How many Asian countries has Cornelia visited?"""
    total_countries = 42
    europe_countries = 20
    southamerica_countries = 10
    remaining_countries = total_countries - europe_countries - southamerica_countries
    asian_countries = remaining_countries / 2
    result = asian_countries
    return result

print(solution())