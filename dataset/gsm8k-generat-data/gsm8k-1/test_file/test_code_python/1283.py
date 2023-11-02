def solution():
    """In a family, there are 2 brothers and 3 sisters. All sisters are the same age, which is 16. One of the brothers is 12 years old, which is half the age of the older brother. What is the total age of all these siblings?"""
    older_brother_age = 24
    younger_brother_age = 12
    sister_age = 16
    total_age = older_brother_age + younger_brother_age + (3 * sister_age)
    result = total_age
    return result

print(solution())