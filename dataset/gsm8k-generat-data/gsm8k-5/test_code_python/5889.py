def solution():
    current_year = 2021  # The current year is 2021
    aziz_age = 36  # Aziz just celebrated his 36th birthday

    # Aziz was born in:
    aziz_birth_year = current_year - aziz_age

    parents_move_year = 1982  # Aziz's parents moved to America in 1982

    # Calculate the number of years Aziz's parents had been living in America before he was born
    years_before_birth = aziz_birth_year - parents_move_year
    result = years_before_birth
    return result

print(solution())