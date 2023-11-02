def solution():
    """Allen is 25 years younger than his mother. In 3 years, the sum of their ages will be 41. What is the present age of Allen's mother?"""
    # Let Allen's age be x
    # Then, his mother's age is x + 25

    # In 3 years, their ages will be x + 3 and x + 28 + 3 = x + 31
    # The sum of their ages in 3 years will be 41, so we have:
    # x + 3 + x + 31 = 41
    # 2x + 34 = 41
    # 2x = 7
    # x = 3.5

    # Allen's age cannot be a decimal, so let's round up to 4
    x = 4

    # Allen's mother's age is x + 25
    mother_age = x + 25

    # Return the result
    return mother_age

print(solution())