def solution():
    thomas_age = 6  # Thomas is 6 years old
    shay_age = thomas_age + 13  # Shay is 13 years older than Thomas
    james_age = shay_age + 5  # James is 5 years older than Shay

    # Calculate the age difference between James and Thomas
    age_difference = james_age - thomas_age

    # Calculate how old James will be when Thomas reaches his current age
    james_future_age = james_age + age_difference
    result = james_future_age
    return result

print(solution())