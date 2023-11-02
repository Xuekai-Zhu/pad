def solution():
    """Allen is 25 years younger than his mother. In 3 years, the sum of their ages will be 41. What is the present age of Allen's mother?"""
    # Let's assume Allen's current age is x
    # Then Allen's mother's current age is x+25
    # In 3 years, Allen's age will be x+3 and his mother's age will be x+28

    # The sum of their ages in 3 years will be 41
    # (x+3) + (x+28) = 41
    # 2x + 31 = 41
    # 2x = 10
    # x = 5

    # Allen's current age is 5, so his mother's current age is 30
    result = 30
    return result

print(solution())