def solution():
    """Rachel is 12 years old, and her grandfather is 7 times her age. Her mother is half grandfather's age, and her father is 5 years older than her mother. How old will Rachel's father be when she is 25 years old?"""
    rachel_age = 12
    grandfather_age = rachel_age * 7
    mother_age = grandfather_age / 2
    father_age = mother_age + 5
    years_passed = 25 - rachel_age
    father_age_25 = father_age + years_passed
    result = father_age_25
    return result

print(solution())