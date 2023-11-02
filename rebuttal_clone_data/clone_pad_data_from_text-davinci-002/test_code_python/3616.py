def solution():
    visited_countries = 42
    europe_countries = 20
    south_america_countries = 10
    asia_countries = visited_countries - europe_countries - south_america_countries
    result = asia_countries / 2
    return result

print(solution())