def solution():
    """Amy, Jeremy, and Chris have a combined age of 132. Amy is 1/3 the age of Jeremy, and Chris is twice as old as Amy. How old is Jeremy?"""
    total_age = 132
    amy_ratio = 1/3
    chris_ratio = 2
    aj_ratio = 1 + amy_ratio
    total_ratio = aj_ratio + chris_ratio
    jeremy_age = total_age / total_ratio * aj_ratio
    result = jeremy_age
    return result

print(solution())