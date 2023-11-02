def solution():
    """The sum of the ages of three boys is 29. If two of the boys are the same age and the third boy is 11 years old, how old are the other two boys?"""
    total_age = 29
    third_boy_age = 11
    two_other_boys_age = (total_age - third_boy_age) / 2
    result = two_other_boys_age
    return result

print(solution())