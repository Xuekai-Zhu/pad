def solution():
    # Find the current age of Harry's father 
    father_age = 50 + 24

    # Find the current age of Harry's mother 
    mother_age = father_age - (1/25)*50

    # Find the age of Harry's mother when she gave birth to him 
    mother_birth_age = mother_age - 50

    result = mother_birth_age
    return result

print(solution())