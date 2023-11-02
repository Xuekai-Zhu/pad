def solution():
    # Find Beth's current age
    beth_age_now = 9 + 5  # Joey will be as old as Beth is now in 5 years

    # Find Joey's age when Beth was Joey's age now
    joey_age_difference = beth_age_now - 9
    joey_age_when_beth_was_joeys_age_now = 9 - joey_age_difference
    result = joey_age_when_beth_was_joeys_age_now
    return result

print(solution())