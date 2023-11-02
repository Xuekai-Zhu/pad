def solution():
    age_difference = 7
    talias_age_in_7_years = 20
    talias_mom_multiplier = 3
    years_from_now = 3

    # Calculate Talia's current age
    talias_age_now = talias_age_in_7_years - age_difference

    # Calculate Talia's mom's current age
    talias_mom_age_now = talias_age_now * talias_mom_multiplier

    # Calculate Talia's father's current age
    talias_father_age_now = talias_mom_age_now - years_from_now

    result = talias_father_age_now
    return result

print(solution())