def solution():
    joey_age_now = 9
    years_from_now = 5

    # Calculate Beth's age now
    beth_age_now = joey_age_now + years_from_now

    # Calculate the age Joey will be when Beth is Joey's current age
    joey_age_when_beth_was_joeys_age_now = beth_age_now - joey_age_now

    # Calculate Joey's age when Beth was Joey's current age
    joey_age_when_beth_was_joeys_age_now -= years_from_now

    result = joey_age_when_beth_was_joeys_age_now
    return result

print(solution())