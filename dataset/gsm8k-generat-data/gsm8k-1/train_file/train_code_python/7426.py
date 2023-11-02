def solution():
    """In 5 years, Joey will be as old as Beth is now. If Joey is 9 now, how old was Joey when Beth was Joey's age now?"""
    joey_age_now = 9
    beth_age_now = joey_age_now + 5  # In 5 years, Joey will be as old as Beth is now
    age_difference = beth_age_now - joey_age_now
    joey_age_then = joey_age_now - age_difference
    result = joey_age_then
    return result

print(solution())