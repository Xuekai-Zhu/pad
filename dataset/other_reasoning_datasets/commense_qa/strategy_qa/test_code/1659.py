def solution():
    rush_limbaugh_start_year = 1988
    coast_to_coast_start_year = 1984
    current_year = 2020
    
    rush_limbaugh_years_on_air = current_year - rush_limbaugh_start_year
    coast_to_coast_years_on_air = current_year - coast_to_coast_start_year
    
    if coast_to_coast_years_on_air > rush_limbaugh_years_on_air:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())