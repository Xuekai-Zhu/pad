def solution():
     mark_age = 7 + 15
     amy_age = 15
     age_difference = mark_age - amy_age
     mark_age_in_5_years = mark_age + 5
     amy_age_in_5_years = amy_age + 5
     new_age_difference = mark_age_in_5_years - amy_age_in_5_years
     result = new_age_difference + age_difference
     return result

print(solution())