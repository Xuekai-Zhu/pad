def solution():
    eddie_birth_year = 1961
    car_phone_common_year = 1984
    max_child_age_to_dial_911 = 12
    if eddie_birth_year + max_child_age_to_dial_911 < car_phone_common_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())