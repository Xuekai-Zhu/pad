def solution():
    """Emily is 20 years old and her older sister, Rachel, is 24 years old. How old is Rachel when Emily is half her age?"""
    # Calculate the age difference between Rachel and Emily
    age_difference = 24 - 20

    # Calculate the age when Emily is half Rachel's age
    half_age = (20 + age_difference / 2)

    # Calculate Rachel's age when Emily is half her age
    rachel_age = half_age + age_difference

    result = rachel_age
    return result

print(solution())