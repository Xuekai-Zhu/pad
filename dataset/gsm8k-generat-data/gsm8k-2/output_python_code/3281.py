def solution():
    """It’s February 2021. Mark was born in January 1976. Graham is 3 years younger than Mark, and Graham’s sister, Janice, is 1/2 the age of Graham. How old is Janice?"""
    mark_birth_year = 1976
    mark_age_in_2021 = 2021 - mark_birth_year
    graham_age_in_2021 = mark_age_in_2021 - 3
    janice_age_in_2021 = graham_age_in_2021 / 2
    result = janice_age_in_2021
    return result

print(solution())