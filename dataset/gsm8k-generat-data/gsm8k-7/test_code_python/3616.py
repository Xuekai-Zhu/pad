def solution():
    total_countries = 42
    europe_countries = 20
    south_america_countries = 10

    # Calculate the number of countries visited that are not in Europe or South America
    non_europe_or_sa_countries = total_countries - europe_countries - south_america_countries

    # Calculate the number of Asian countries visited
    asian_countries = non_europe_or_sa_countries / 2

    result = asian_countries
    return result

print(solution())