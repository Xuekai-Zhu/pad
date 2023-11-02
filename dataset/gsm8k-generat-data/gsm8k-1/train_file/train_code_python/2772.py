def solution():
    """Justin is 26 years old. When he was born his elder sister Jessica was 6 years old.
    James is their elder brother and is 7 years older than Jessica. How old will James be after 5 years?"""
    justin_age = 26
    jessica_age = justin_age - 6
    james_age = jessica_age + 7
    james_age_after_5_years = james_age + 5
    result = james_age_after_5_years
    return result

print(solution())