def solution():
    """The sum of the ages of Jeremy, Sebastian and Sophia in three years is 150. Currently, Sebastian is 4 years older than Jeremy. If Jeremy's age is 40, calculate Sophia's age three years from now?"""
    jeremy_age = 40
    sebastian_age = jeremy_age + 4
    sophia_age_in_three_years = 150 - (jeremy_age + sebastian_age + 3 * 2)
    sophia_age = sophia_age_in_three_years - 3
    result = sophia_age
    return result

print(solution())