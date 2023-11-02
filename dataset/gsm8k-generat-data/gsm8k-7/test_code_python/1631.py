def solution():
    john_age = 10
    sister_age = john_age * 2
    age_difference = sister_age - john_age
    future_age_difference = 50 - john_age
    sister_future_age = sister_age + future_age_difference
    result = sister_future_age
    return result

print(solution())