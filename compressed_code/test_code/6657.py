def solution():
    
    younger_brother_age_when_Viggo_was_2 = 2
    current_younger_brother_age = 10
    difference_in_age = current_younger_brother_age - younger_brother_age_when_Viggo_was_2
    viggo_age_when_brother_was_2 = 2 * younger_brother_age_when_Viggo_was_2 + 10
    viggo_current_age = viggo_age_when_brother_was_2 + difference_in_age
    sum_of_ages = viggo_current_age + current_younger_brother_age
    result = sum_of_ages
    return result

print(solution())