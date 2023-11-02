def solution():
    emily_age = 20
    rachel_age = 24
    age_difference = rachel_age - emily_age

    # Calculate when Emily is half Rachel's age
    half_age = emily_age + age_difference / 2
    rachel_age_when_half = rachel_age + age_difference / 2
    result = rachel_age_when_half
    return result

print(solution())