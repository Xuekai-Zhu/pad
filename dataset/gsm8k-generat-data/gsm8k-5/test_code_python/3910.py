def solution():
    mason_age = 20  # Mason is 20 years old
    sydney_age = 3 * mason_age  # Sydney is three times younger than Mason
    mason_father_age = sydney_age + 6  # Sydney is six years younger than Mason's father
    father_age = mason_father_age + mason_age  # Calculate the age of Mason's father
    result = father_age
    return result

print(solution())