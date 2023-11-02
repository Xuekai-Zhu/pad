def solution():
    """Michael has two brothers. His oldest brother is 1 year older than twice Michael's age when Michael was a year younger. His younger brother is 5 years old, which is a third of the age of the older brother. What is their combined age?"""
    younger_brother_age = 5
    older_brother_age = younger_brother_age * 3
    michael_age = older_brother_age / 2 - 1
    total_age = michael_age + older_brother_age + younger_brother_age
    result = total_age
    return result

print(solution())