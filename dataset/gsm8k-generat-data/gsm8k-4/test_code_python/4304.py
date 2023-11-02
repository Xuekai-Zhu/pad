def solution():
    """Rachel is 12 years old, and her grandfather is 7 times her age. Her mother is half grandfather's age, and her father is 5 years older than her mother. How old will Rachel's father be when she is 25 years old?"""
    # Calculate the age of the grandfather
    grandfather_age = 12 * 7

    # Calculate the age of the mother
    mother_age = grandfather_age / 2

    # Calculate the age of the father
    father_age = mother_age + 5

    # Calculate the number of years until Rachel is 25 years old
    years_until_25 = 25 - 12

    # Calculate the age of Rachel's father when she is 25 years old
    father_age_at_25 = father_age + years_until_25

    result = father_age_at_25
    return result

print(solution())