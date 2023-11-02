def solution():
    islamic_dominated_countries = ["Iran", "Saudi Arabia", "Pakistan", "Egypt", "Indonesia", "Bangladesh"]
    starbucks_locations = {"USA", "China", "United Arab Emirates (Dubai)"}
    overlap = [country for country in islamic_dominated_countries if country in starbucks_locations]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())