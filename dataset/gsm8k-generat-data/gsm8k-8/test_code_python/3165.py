def solution():
    # Define Talia's age in seven years and her mom's current age
    talia_age_in_7_years = 20
    mom_age = 3 * (talia_age_in_7_years - 7)

    # Calculate Talia's current age
    talia_age = talia_age_in_7_years - 7

    # Calculate the difference in years between Talia's mom and dad
    dad_mom_age_diff = 3

    # Calculate Talia's dad's current age
    dad_age = mom_age - dad_mom_age_diff

    result = dad_age 
    return result

print(solution())