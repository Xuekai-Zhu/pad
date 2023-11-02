def solution():
    """Cornelia likes to travel. She visited already 42 different countries. 20 of them were in Europe and 10 in South America. From the rest of the countries, only half of them were in Asia. How many Asian countries has Cornelia visited?"""
    # Define the number of countries visited in Europe and South America
    europe_countries = 20
    south_america_countries = 10

    # Calculate the number of countries visited in other continents
    other_countries = 42 - europe_countries - south_america_countries

    # Calculate the number of Asian countries visited
    asian_countries = other_countries / 2

    # Display the number of Asian countries visited
    result = asian_countries
    return result

print(solution())