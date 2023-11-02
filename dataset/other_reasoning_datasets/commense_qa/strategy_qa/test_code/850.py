def solution():
    social_democratic_party_founded_year = 1863
    frederick_II_reign_years = (1740, 1786)
    if social_democratic_party_founded_year > frederick_II_reign_years[0]:
        result = "no"
    else:
        result = "not enough information"
    return result

print(solution())