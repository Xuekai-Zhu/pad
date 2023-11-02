def solution():
    emily_age = 20
    rachel_age = 24

    # Calculate the age difference between Rachel and Emily
    age_diff = rachel_age - emily_age

    # Calculate the age when Emily is half Rachel's age
    half_age = rachel_age / 2
    age_when_half = half_age - age_diff

    result = age_when_half
    return result

print(solution())