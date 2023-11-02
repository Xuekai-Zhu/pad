def solution():
    """Seth is twice as old as Brooke. In 2 years, the sum of their ages will be 28. How old is Seth?"""
    sum_of_ages = 28
    age_difference = 2
    # Let x be Brooke's age.
    # Then Seth's age is 2x.
    # In 2 years, their ages will be x+2 and 2x+2.
    # So, x+2 + 2x+2 = 28 - age_difference*2
    x = (sum_of_ages - age_difference*2 - 4) / 3
    seth_age = 2*x
    result = seth_age
    return result

print(solution())