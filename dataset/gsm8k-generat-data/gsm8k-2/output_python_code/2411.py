def solution():
    """Mike is 16 years old. His sister Barbara is half as old as he is. How old is Barbara going to be when Mike is 24 years old?"""
    mike_age = 16
    barbara_age = mike_age / 2
    age_difference = 24 - mike_age
    barbara_future_age = barbara_age + age_difference
    result = barbara_future_age
    return result

print(solution())