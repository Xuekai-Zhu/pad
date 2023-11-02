def solution():
    total_countries = 42  # total number of countries visited
    europe_countries = 20  # number of countries visited in Europe
    south_america_countries = 10  # number of countries visited in South America
    rest_countries = total_countries - europe_countries - south_america_countries  # number of countries visited outside Europe and South America
    asian_countries = rest_countries // 2  # number of Asian countries visited (assuming only half of rest of the countries were in Asia)
    result = asian_countries
    return result

print(solution())