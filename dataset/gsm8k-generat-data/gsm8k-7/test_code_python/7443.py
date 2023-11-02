def solution():
    harry_age = 50
    father_age_difference = 24
    mother_father_age_difference_ratio = 1 / 25

    # Calculate the father's current age
    father_age = harry_age + father_age_difference

    # Calculate the mother's current age
    mother_age = father_age - (harry_age * mother_father_age_difference_ratio)

    # Calculate the age of the mother when she gave birth to Harry
    mother_harry_age_difference = father_age_difference - harry_age
    mother_birth_age = mother_age - mother_harry_age_difference

    result = mother_birth_age
    return result

print(solution())