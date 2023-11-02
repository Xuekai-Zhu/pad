def solution():
    first_skyscraper = 100
    current_year = 2020
    year_of_200th_anniversary = first_skyscraper + 200
    years_until_5_years_before_200th_anniversary = year_of_200th_anniversary - 5 - current_year
    result = years_until_5_years_before_200th_anniversary
    return result

print(solution())