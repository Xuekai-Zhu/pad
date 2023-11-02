def solution():
    total_countries = 42  # Cornelia visited 42 countries
    europe_countries = 20  # Out of those 42, 20 were in Europe
    south_america_countries = 10  # and 10 were in South America
    rest_of_countries = total_countries - europe_countries - south_america_countries  # Rest of the countries that Cornelia visited

    asia_countries = rest_of_countries / 2  # Half of the rest of the countries that Cornelia visited were in Asia
    result = asia_countries
    return result

print(solution())