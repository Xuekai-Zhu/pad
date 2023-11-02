def solution():
    """John is half times younger than his father, who is 4 years older than John's mother. If John's father is 40 years old, what's the age difference between John and his mother?"""
    father_age = 40
    mother_age = father_age - 4
    john_age = father_age / 2
    age_difference = john_age - mother_age
    result = age_difference
    return result

print(solution())