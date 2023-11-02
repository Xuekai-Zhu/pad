def solution():
    """Rachel is 12 years old, and her grandfather is 7 times her age. Her mother is half grandfather's age, and her father is 5 years older than her mother. How old will Rachel's father be when she is 25 years old?"""
    # Define Rachel's current age and grandfather's age
    rachel_age = 12
    grandfather_age = 7 * rachel_age

    # Calculate mother's age and father's age
    mother_age = 0.5 * grandfather_age
    father_age = mother_age + 5

    # Calculate the age difference between Rachel and her father
    age_difference = father_age - rachel_age

    # Calculate Rachel's father's age when she is 25
    father_age_at_25 = father_age + (25 - rachel_age)

    # Display Rachel's father's age at 25
    result = father_age_at_25
    return result

print(solution())