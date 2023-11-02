def solution():
    """John is 10 years old. His sister is twice his age. When he is 50 years old, how old will his sister be?"""
    john_age = 10
    sister_age = 2 * john_age
    age_difference = sister_age - john_age
    future_age_difference = 50 - john_age
    sister_future_age = sister_age + future_age_difference
    result = sister_future_age
    return result

print(solution())