def solution():
    """Justin is 26 years old. When he was born his elder sister Jessica was 6 years old. James is their elder brother and is 7 years older than Jessica. How old will James be after 5 years?"""
    jessica_age_diff = 26 - 6  # Jessica is 20 now
    james_age_diff = jessica_age_diff + 7  # James is 27 now
    james_age_after_5_years = james_age_diff + 5  # James will be 32
    result = james_age_after_5_years
    return result

print(solution())