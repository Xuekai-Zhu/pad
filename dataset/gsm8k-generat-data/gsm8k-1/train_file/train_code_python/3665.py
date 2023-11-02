def solution():
    """Jordan's dog, Max, was born on the same day that Luka turned 4 years old. Luka is exactly 2 years older than is Aubrey. On Aubrey's 8th birthday, how many years old was Jordan's dog, Max?"""
    aubrey_age = 8
    luka_age = aubrey_age + 2
    max_age = luka_age - 4 + aubrey_age
    result = max_age
    return result

print(solution())