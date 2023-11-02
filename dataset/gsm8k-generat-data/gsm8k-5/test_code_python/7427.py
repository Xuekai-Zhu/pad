def solution():
    # Determine how old Beth is now
    beth_now = 9 + 5  # In 5 years, Joey will be as old as Beth is now

    # Determine how old Joey was when Beth was Joey's age now
    age_difference = beth_now - 9  # Joey is currently 9 years old
    joey_previous_age = 9 - age_difference

    result = joey_previous_age
    return result

print(solution())