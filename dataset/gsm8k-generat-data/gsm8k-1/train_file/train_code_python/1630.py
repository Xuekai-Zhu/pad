def solution():
    """John is 10 years old. His sister is twice his age. When he is 50 years old, how old will his sister be?"""
    john_age = 10
    sister_age = john_age * 2
    age_difference = sister_age - john_age
    future_age = 50
    future_sister_age = sister_age + (future_age - john_age)
    result = future_sister_age
    return result

print(solution())