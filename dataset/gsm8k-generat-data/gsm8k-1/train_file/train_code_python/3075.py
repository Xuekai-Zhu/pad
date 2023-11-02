def solution():
    """Emily is 20 years old and her older sister, Rachel, is 24 years old. How old is Rachel when Emily is half her age?"""
    emily_age = 20
    rachel_age = 24
    age_difference = rachel_age - emily_age
    half_emily_age = emily_age / 2
    rachel_age_half_emily_age = rachel_age + age_difference
    while rachel_age_half_emily_age != half_emily_age:
        rachel_age += 1
        emily_age += 1
        rachel_age_half_emily_age = rachel_age + age_difference
    result = rachel_age
    return result

print(solution())