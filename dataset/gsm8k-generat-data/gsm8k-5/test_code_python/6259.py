def solution():
    father_age = 40  # John's father is 40 years old
    mother_age = father_age - 4  # John's mother is 4 years younger than his father
    john_age = father_age / 2  # John is half times younger than his father

    # Calculate the age difference between John and his mother
    age_difference = john_age - mother_age
    result = age_difference
    return result

print(solution())