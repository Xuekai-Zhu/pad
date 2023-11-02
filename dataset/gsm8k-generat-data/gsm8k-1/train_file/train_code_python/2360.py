def solution():
    """Martha met Ellen in the grocery store alone and asked her age. Martha realized she was twice as old as Ellen will be in six years. If Ellen is 10 years old now, calculate Martha's age now."""
    ellen_age = 10
    ellen_future_age = ellen_age + 6
    martha_age = 2 * ellen_future_age
    result = martha_age
    return result

print(solution())