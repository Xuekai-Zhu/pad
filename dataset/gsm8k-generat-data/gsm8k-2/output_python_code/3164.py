def solution():
    """In seven years, Talia will be 20 years old. Talia's mom is currently three times as old as Talia is today. In three years, Talia's father will be the same age as Talia's mom is today. Currently, how many years old is Talia's father?"""
    talia_age_in_7_years = 20
    talia_age_now = talia_age_in_7_years - 7
    mom_age_now = talia_age_now * 3
    father_age_now = mom_age_now + 3
    result = father_age_now
    return result

print(solution())