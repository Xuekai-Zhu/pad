def solution():
    
    total_countries = 42
    europe_countries = 20
    southamerica_countries = 10
    remaining_countries = total_countries - europe_countries - southamerica_countries
    asian_countries = remaining_countries / 2
    result = asian_countries
    return result

print(solution())