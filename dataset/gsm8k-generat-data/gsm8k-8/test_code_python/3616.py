def solution():
    # Define the number of countries visited in Europe and South America
    europe_countries = 20
    south_america_countries = 10

    # Calculate the total number of countries visited
    total_countries = 42

    # Calculate the number of countries visited outside of Europe and South America
    other_countries = total_countries - europe_countries - south_america_countries

    # Calculate the number of Asian countries visited
    asian_countries = other_countries / 2

    result = asian_countries
    return result

print(solution())