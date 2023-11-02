def solution():
    
    earnings = 5000000
    bonus_total = 0.25 * earnings
    total_females = (2/3) * 3300
    female_mothers = total_females - 1200
    bonus_per_female_mother = bonus_total / female_mothers
    result = bonus_per_female_mother
    return result

print(solution())