def solution():
    """Cornelia likes to travel. She visited already 42 different countries. 20 of them were in Europe and 10 in South America. From the rest of the countries, only half of them were in Asia. How many Asian countries has Cornelia visited?"""
    # Define the total number of countries visited
    total_countries = 42

    # Define the number of countries visited in Europe and South America
    europe_countries = 20
    sa_countries = 10

    # Calculate the number of countries visited outside Europe and South America
    non_es_countries = total_countries - europe_countries - sa_countries

    # Calculate the number of Asian countries visited
    asian_countries = non_es_countries / 2

    # return the result
    result = asian_countries
    return result

print(solution())