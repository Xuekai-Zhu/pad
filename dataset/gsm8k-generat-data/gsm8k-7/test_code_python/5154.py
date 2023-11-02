def solution():
    thomas_age = 6
    shay_age = thomas_age + 13
    james_age = shay_age + 5

    # Calculate the age difference between James and Thomas
    age_difference = james_age - thomas_age

    # Calculate how old James will be when Thomas reaches his age
    james_future_age = james_age + age_difference
    result = james_future_age
    return result

print(solution())