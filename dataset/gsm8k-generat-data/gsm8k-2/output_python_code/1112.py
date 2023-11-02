def solution():
    """Viggo's age was 10 years more than twice his younger brother's age when his brother was 2. If his younger brother is currently 10 years old, what's the sum of theirs ages?"""
    brother_age = 10
    viggo_age = 10 + 2 * (brother_age - 2)
    total_age = brother_age + viggo_age
    result = total_age
    return result

print(solution())