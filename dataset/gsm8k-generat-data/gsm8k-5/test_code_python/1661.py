def solution():
    anniversary_year = 2025  # Tim and Donna will celebrate their 20th wedding anniversary in 2025
    married_year = anniversary_year - 20  # They got married 20 years ago
    dating_years = 3  # They dated for 3 years before getting married
    met_years = 2  # They met 2 years before dating

    # Calculate the year they started dating
    dating_year = married_year - dating_years

    # Calculate the year they met
    met_year = dating_year - met_years
    result = met_year
    return result

print(solution())