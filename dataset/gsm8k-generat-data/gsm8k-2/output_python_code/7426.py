def solution():
    """In 5 years, Joey will be as old as Beth is now. If Joey is 9 now, how old was Joey when Beth was Joey's age now?"""
    joey_age_now = 9
    beth_age_now = 5 + joey_age_now
    joey_age_when_beth_is_now = beth_age_now - 5
    joey_age_difference = joey_age_now - joey_age_when_beth_is_now
    joey_age_when_beth_was_joeys_age = joey_age_now - joey_age_difference
    result = joey_age_when_beth_was_joeys_age
    return result

print(solution())