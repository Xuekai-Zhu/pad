def solution():
    """In 7 years, Kaylee will be 3 times as old as Matt is now. If Matt is currently 5 years old, how old is Kaylee now?"""
    current_age_matt = 5
    age_difference = 3
    kaylee_age_in_7_years = current_age_matt * age_difference
    kaylee_current_age = kaylee_age_in_7_years - 7
    result = kaylee_current_age
    return result

print(solution())