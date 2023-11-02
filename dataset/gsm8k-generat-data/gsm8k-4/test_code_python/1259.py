def solution():
    """Ryanne is 7 years older than Hezekiah. Together Ryanne's and Hezekiah's ages equal 15 years. How many years old is Hezekiah?"""
    # Let's assume Hezekiah's age to be x
    x = 0

    # Let's assume Ryanne's age to be x + 7
    y = x + 7

    # Their total age is 15
    x + y = 15

    # Substituting the value of y
    x + (x + 7) = 15

    # Simplifying the equation
    2x + 7 = 15

    # Solving for x
    x = 4

    # Hezekiah is 4 years old
    result = x
    return result

print(solution())