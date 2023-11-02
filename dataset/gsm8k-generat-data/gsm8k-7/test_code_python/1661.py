def solution():
    anniversary_year = 2025
    married_year = anniversary_year - 20
    dating_years = 3
    met_years = 2

    # Calculate the year when they started dating
    dating_year = married_year - dating_years

    # Calculate the year when they met
    met_year = dating_year - met_years
    result = met_year
    return result

print(solution())