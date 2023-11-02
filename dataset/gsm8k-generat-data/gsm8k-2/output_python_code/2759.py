def solution():
    """Joel is 5 years old and his dad is 32 years old. How old will Joel be when his dad is twice as old as him?"""
    joel_age = 5
    dad_age = 32
    age_diff = dad_age - joel_age
    double_age_diff = age_diff * 2
    dad_double_age = dad_age + double_age_diff
    joel_double_age = dad_double_age - age_diff
    joel_double_age_diff = joel_double_age - joel_age
    result = joel_double_age_diff
    return result

print(solution())