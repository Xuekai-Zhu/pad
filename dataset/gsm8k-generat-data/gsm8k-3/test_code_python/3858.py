def solution():
    """Three years ago, Bethany was twice the age of her younger sister. In 5 years, her younger sister will be 16. How old is Bethany now?"""
    # Let x be the age of Bethany's younger sister now
    # Bethany was twice her sister's age three years ago
    # This means Bethany is 3 years older than twice her sister's age now
    # In 5 years, Bethany's sister will be 16, so her current age is 16 - 5 = 11
    # Therefore, Bethany's age is 3 + 2 * 11 = 25

    bethany_age = 3 + 2 * 11
    result = bethany_age
    return result

print(solution())