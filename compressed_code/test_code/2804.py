def solution():
    
    total_countries = 42
    europe_countries = 20
    south_america_countries = 10
    rest_countries = total_countries - europe_countries - south_america_countries
    asia_countries = rest_countries / 2
    result = asia_countries
    return result

print(solution())