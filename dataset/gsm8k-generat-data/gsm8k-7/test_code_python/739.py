def solution():
    blood_needed_weekly = 7 * 128  # 7 gallons of blood = 7 x 128 fluid ounces
    blood_needed_daily = blood_needed_weekly / 7
    blood_per_person = 2 * 8  # 2 pints of blood = 2 x 16 fluid ounces
    people_needed_daily = blood_needed_daily / blood_per_person
    result = people_needed_daily
    return result

print(solution())