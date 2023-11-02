def solution():
    """Three years ago, Bethany was twice the age of her younger sister. In 5 years, her younger sister will be 16. How old is Bethany now?"""
    # Define Bethany's age three years ago as x
    x = 2

    # Define the current age of Bethany's younger sister as y
    y = 16 - 5

    # Use the relationship between their ages three years ago to solve for Bethany's age now
    bethany_age = 2 * (y + 3) + 3

    result = bethany_age
    return result

print(solution())