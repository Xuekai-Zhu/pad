def solution():
    """Ann is 6 years old. Her brother Tom is now two times older. What will be the sum of their ages 10 years later?"""
    # Calculate Tom's current age
    tom_age = 2 * 6 # Tom is two times older than Ann

    # Calculate their ages 10 years later
    ann_age_after_10_years = 6 + 10
    tom_age_after_10_years = tom_age + 10

    # Calculate the sum of their ages after 10 years
    total_age_after_10_years = ann_age_after_10_years + tom_age_after_10_years

    # Display the sum of their ages after 10 years
    result = total_age_after_10_years
    return result

print(solution())