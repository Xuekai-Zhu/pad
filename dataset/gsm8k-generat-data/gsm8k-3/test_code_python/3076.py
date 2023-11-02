def solution():
    """Emily is 20 years old and her older sister, Rachel, is 24 years old.  How old is Rachel when Emily is half her age?"""
    # Define Emily and Rachel's current ages
    emily_age = 20
    rachel_age = 24

    # Determine the age difference between Emily and Rachel
    age_difference = rachel_age - emily_age

    # Calculate the age at which Emily will be half Rachel's age
    half_age = (rachel_age + age_difference) / 2

    # Determine Rachel's age at that time
    rachel_half_age = half_age + age_difference

    # Display Rachel's age at the time Emily is half her age
    result = int(rachel_half_age)
    return result

print(solution())