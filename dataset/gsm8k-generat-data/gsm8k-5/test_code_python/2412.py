def solution():
    mike_age = 16  # Mike is 16 years old
    barbara_age = mike_age / 2  # Barbara is half as old as Mike
    age_difference = 24 - mike_age  # Mike will be 24 years old in this many years
    barbara_future_age = barbara_age + age_difference  # Calculate how old Barbara will be when Mike is 24

    result = barbara_future_age
    return result

print(solution())