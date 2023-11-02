def solution():
    """In seven years, Talia will be 20 years old. Talia's mom is currently three times as old as Talia is today. In three years, Talia's father will be the same age as Talia's mom is today. Currently, how many years old is Talia's father?"""
    talia_in_7_years = 20
    talia_today = talia_in_7_years - 7
    mom_today = talia_today * 3
    father_in_3_years = mom_today
    father_today = father_in_3_years - 3
    result = father_today
    return result

print(solution())