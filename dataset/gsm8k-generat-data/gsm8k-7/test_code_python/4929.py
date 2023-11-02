def solution():
    john_age = 39

    # Calculate James' age 6 years from now
    james_future_age = (john_age - 3) / 2 + 6

    # Calculate James' age now
    james_current_age = james_future_age - 6

    # Calculate James' older brother's age
    older_brother_age = james_current_age + 4

    result = older_brother_age
    return result

print(solution())