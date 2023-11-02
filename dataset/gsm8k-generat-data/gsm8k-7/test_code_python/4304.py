def solution():
    rachel_age = 12
    grandfather_age = rachel_age * 7
    mother_age = grandfather_age / 2
    father_age = mother_age + 5

    # Calculate the age difference between Rachel and her father
    age_difference = father_age - rachel_age

    # Calculate the age of Rachel's father when she is 25 years old
    father_age_in_25_years = father_age + (25 - rachel_age)

    result = father_age_in_25_years
    return result

print(solution())