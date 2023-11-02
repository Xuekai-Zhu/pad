def solution():
    """
    Aziz's parents moved to America in 1982. The year is 2021 and Aziz just celebrated his 36th birthday. How many years had his parents been living in America before Aziz was born?
    """
    year_moved_to_US = 1982
    current_year = 2021
    aziz_age = 36
    years_parents_lived_in_US_before_aziz_birth = aziz_age - (current_year - year_moved_to_US)

    return years_parents_lived_in_US_before_aziz_birth

print(solution())