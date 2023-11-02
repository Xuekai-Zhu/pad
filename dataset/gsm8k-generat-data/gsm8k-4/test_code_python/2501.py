def solution():
    """Ann is 6 years old. Her brother Tom is now two times older. What will be the sum of their ages 10 years later?"""
    # Define Ann's age
    ann_age = 6

    # Calculate Tom's age
    tom_age = ann_age * 2

    # Calculate their ages 10 years later
    ann_age_new = ann_age + 10
    tom_age_new = tom_age + 10

    # Calculate the sum of their ages
    age_sum = ann_age_new + tom_age_new

    result = age_sum
    return result

print(solution())