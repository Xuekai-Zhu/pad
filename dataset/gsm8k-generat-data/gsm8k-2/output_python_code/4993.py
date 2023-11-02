def solution():
    """Amy, Jeremy, and Chris have a combined age of 132. Amy is 1/3 the age of Jeremy, and Chris is twice as old as Amy. How old is Jeremy?"""
    combined_age = 132
    j = age_jeremy = 3 * (combined_age / 8)
    age_amy = age_jeremy / 3
    age_chris = 2 * age_amy
    result = age_jeremy
    return result

print(solution())