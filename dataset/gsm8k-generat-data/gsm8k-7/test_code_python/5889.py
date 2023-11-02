def solution():
    current_year = 2021
    aziz_age = 36
    parents_move_year = 1982

    # Calculate the number of years since his parents moved to America
    years_in_america = current_year - parents_move_year

    # Calculate the number of years before Aziz was born
    years_before_aziz = years_in_america - aziz_age
    result = years_before_aziz
    return result

print(solution())