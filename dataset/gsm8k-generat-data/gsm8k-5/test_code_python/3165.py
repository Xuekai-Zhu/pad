def solution():
    talia_age_in_7_years = 20  # In 7 years, Talia will be 20
    talia_age_today = talia_age_in_7_years - 7  # Talia's current age
    mom_age_today = 3 * talia_age_today  # Talia's mom is currently three times as old as Talia
    father_age_in_3_years = mom_age_today  # In 3 years, Talia's father will be the same age as Talia's mom is today
    father_age_today = father_age_in_3_years - 3  # Calculate Talia's father's current age

    result = father_age_today
    return result

print(solution())