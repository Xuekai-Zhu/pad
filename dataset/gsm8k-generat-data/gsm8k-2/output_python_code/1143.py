def solution():
    """Michael has two brothers. His oldest brother is 1 year older than twice Michael's age when Michael was a year younger. His younger brother is 5 years old, which is a third of the age of the older brother. What is their combined age?"""
    younger_brother_age = 5
    older_brother_age = younger_brother_age * 3
    michael_age = (older_brother_age - 1) / 2
    age_sum = younger_brother_age + older_brother_age + michael_age
    result = age_sum
    return result

print(solution())