def solution():
    # Calculate grandfather's age
    grandfather_age = 7 * 12

    # Calculate mother's age
    mother_age = 0.5 * grandfather_age

    # Calculate father's age
    father_age = mother_age + 5

    # Calculate the age difference between Rachel and her father
    age_difference = father_age - 12

    # Calculate the age of Rachel's father when she is 25
    father_age_at_25 = age_difference + 25

    result = father_age_at_25
    return result

print(solution())