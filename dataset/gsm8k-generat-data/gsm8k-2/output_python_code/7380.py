def solution():
    """Jessica was half her mother's age when her mother died. If her mother were alive now, ten years later, she would have been 70. How old is Jessica currently?"""
    mother_age_when_died = 2 * (70 - 10)
    jessica_age_now = mother_age_when_died / 2
    result = jessica_age_now
    return result

print(solution())