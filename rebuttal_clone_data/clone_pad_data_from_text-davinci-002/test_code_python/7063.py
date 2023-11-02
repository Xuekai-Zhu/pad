def solution():
    male_employees = 1100
    female_employees = 1200
    total_employees = 3300
    percent_bonus = 25
    facebook_earnings = 5000000
    bonus_amount = facebook_earnings * (percent_bonus / 100)
    non_mother_employees = female_employees - 1200
    total_mothers = total_employees - male_employees - non_mother_employees
    bonus_per_mother = bonus_amount / total_mothers
    result = bonus_per_mother
    return result

print(solution())